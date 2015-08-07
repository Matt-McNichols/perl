#! /usr/bin/perl
use warnings;
use strict;


if($#ARGV > 2 or $ARGV[0]=~/-*help/){
print"
This script creates a header for verilog or C files and makes a simple
code skeleton for the selected code type. If the file you are attempting
to create a header for already has existing code writen, this script
will just prepend the header to the existing file.
 
  Usage: mkhdr.pl [file name][file type]
   
   Where:
     -c = C file
     -v = Verilog file.

";
}


my $file_name = $ARGV[0];

if((-e $file_name) || (-s $file_name)){
  print"File Exists \n";
#the double '>>' below just opens the file, without deleting the whole thing
  open(CODE_FILE,"$file_name")||die("can't open the existing file $file_name");
}
else{
  print"file does not exist\n";
  exit;
#the single '>' below kills the file and opens it for r/w
#chmod 777,$file_name or print(" Couldn't change permissions on $file_name you will need to do that yourself :-)");
}



#####  Phase one add file to report.txt
#
my $line;
my $module_ports=0;
my $in_module=0;
my $in_inst=0;


open(my $file_out, '>>', 'hierarchy_report.txt');
print $file_out "File Name:  ".$file_name."\n";
while(<CODE_FILE>)
{
#The text being printed to output file
#is controlled from here
  $line=$_;

# Keep printing until module ports are declared
  if($module_ports==1 and $in_inst==0){
    if($line =~ '.*\);')
    { 
      $module_ports=0;
      print $file_out "\t".$line."\n";
    }
    else
    {
      print $file_out "\t".$line;
    }
  }
  elsif($in_module==1 and $in_inst==1){
    if($line =~ '.*\);')
    {
      $in_inst=0;
      print $file_out "\t\t".$line."\n";
    }
    else
    {
      print $file_out "\t\t".$line;
    }
  }


  if($line =~ 'module\s.*\s' and $in_module==0  )
  {
    $in_module=1;
    if($module_ports== 0 and !($line =~ '.*\);'))
    {
      $module_ports=1;
      print $file_out "\t".$line;
    }
    else
    {
      print $file_out "\t".$line."\n";
    }
  }
  elsif($line =~ '.\S\s\S*\(' and $in_module==1 and $module_ports==0 and $in_inst==0 and !($line =~ m/(if|else if|while|@|for|assign|=|case|\/\/|\/\*|\*\/)|function/ ))
  {
    if($in_inst== 0 and !($line =~ '.*\);'))
    {
      $in_inst=1;
      print $file_out "\t\tINSTANCE
\t\t".$line;
    }
    else
    {
      print $file_out "\t\t".$line."\n";
    }
  }
  elsif($line =~ 'endmodule')
  {
    print $file_out "\t".$line."\n\n";
    $in_module=0;
  }
#print $file_out $in_module."\t".$module_ports."\t".$in_inst."\n";
}
close CODE_FILE;
close $file_out;


#declare variables for second section
#my $line_prev;
my $hold_location;
my $inst_type;
my $inst_name;
my $inst_not_found=1;
$line="";





####  Phase two find the file name of each instance origin.
open(my $v_report, '>', 'verilog_report.txt');
open(HIER_REPORT,"hierarchy_report.txt")||die("can't open the existing file hierarchy_report.txt ");


while(<HIER_REPORT>)
{
  $line=$_;
#print file name and module
  if($line =~ m/File Name/)
  {
    print $v_report $line;
    $line=<HIER_REPORT>;
    print $v_report $line;
  }
  elsif($line =~ m/module/)
  {
    print $v_report $line."\n";
  }
  elsif($line=~/INSTANCE/)
  {
#store the instance type
#    $line=~ m/\s(.*)\(/;
#    $inst_type=$1;
    print $v_report $line;
    $line=<HIER_REPORT>;

    if($line !~ /#\(/)
    {
      print $v_report $line."\n";
    }
    else
    {
      print $v_report $line;
      $line=<HIER_REPORT>;
      $hold_location=tell($line);
      seek(HIER_REPORT,0,0);
      while(<HIER_REPORT>)
      {
        $inst_name=$_;
#print $v_report $inst_name;
        if($inst_name !~ /\.|\(|\)|\/\/|^$|^\s*$/)
        {
          print $v_report $inst_name."\n";
          $inst_not_found=0;
          last;
        }
      }
      seek(HIER_REPORT,$hold_location,0);
      if($inst_not_found==1)
      {
        print $v_report "**Error:  instance not found\n";
        last;
      }
    }
  }
  elsif($line=~/endmodule/)
  {
    print $v_report $line;
    print $v_report "---------------------------\n";
  }
 
}
close HIER_REPORT;
close $v_report;







