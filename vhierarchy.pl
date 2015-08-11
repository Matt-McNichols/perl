#! /usr/bin/perl
use Class::Struct;
use warnings;
use strict;

my @list;
my $i=0;
my $file_name_top;


if($#ARGV==-1)
{
  @list= `ls`;
  while($list[$i])
  {
    chomp($list[$i]);
    if ($list[$i] =~ m/.*\.v/)
    {
my $call_wo_arg = get_hier($list[$i]);
    }
    $i++;
  }
my $v_report=verilog_report();
  exit;
}
elsif($#ARGV > 2 or $ARGV[0]=~/-*help/){
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
elsif ($#ARGV==0)
{
$file_name_top = $ARGV[0];
my $call_w_arg = get_hier($file_name_top);
my $v_report=verilog_report();
}
elsif ($#ARGV==1 && $ARGV[0]=~m/ss|-ss/)
{
  @list= `ls`;
  while($list[$i])
  {
    chomp($list[$i]);
    if ($list[$i] =~ m/.*\.v/)
    {
my $call_wo_arg = get_hier($list[$i]);
    }
    $i++;
  }
  my $call_sig_trace=signal_trace($ARGV[1]);
  exit;
}
else
{
  print"you entered something wrong";
  exit;
}
#start of function



sub get_hier
{
my $file_name=$_[0];
#print $file_name;

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
print $file_out "\n\nFile Name:  ".$file_name."\n";
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
  elsif($line =~ '.\S\s\S*\(' and $in_module==1 and $module_ports==0 and $in_inst==0 and !($line =~ m/\Wif\(|\Wif\s\(|begin|else if|while|@|for|assign|=|case|\/\/|\/\*|\*\/|function|&|\-|\(\(|\)\)|\`|!/ ))
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
}







sub verilog_report
{
#declare variables for second section
#my $line_prev;
my $hold_location;
my $inst_type;
my $inst_name;
my $inst_not_found=1;
my $line="";





####  Phase two find the file name of each instance origin.
open(my $v_report, '>', 'verilog_report.txt');
open(HIER_REPORT,"hierarchy_report.txt")||die("can't open the existing file hierarchy_report.txt ");


while(<HIER_REPORT>)
{
  $line=$_;
#print file name and module
  if($line =~ m/File Name/)
  {
    print $v_report "---------------------------\n";
    print $v_report $line;
    $line=<HIER_REPORT>;
    print $v_report $line;
  }
  elsif(($line =~ m/module/)&&($line !~ m/endmodule/))
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
#     $hold_location=tell($line);
#seek(HIER_REPORT,0,0);
      while(<HIER_REPORT>)
      {
        $inst_name=$_;
#print $v_report $inst_name;
        if($inst_name !~ /\.|\)$|\)\s*$|\/\/|^$|^\s*$/)
        {
          print $v_report $inst_name."\n";
          $inst_not_found=0;
          last;
        }
      }
#      seek(HIER_REPORT,$hold_location,0);
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
    print $v_report "---------------------------\n\n\n";
  }
}
close HIER_REPORT;
close $v_report;

}


sub signal_trace
{
#string does not have new line
  my $trace_signal=$_[0];
  my $trace_file;
  my $trace_module="NO MOD";
  my $trace_inst;
  my $line;

  print("in signal trace\n");
  print("string passed in:".$_[0]."\n");

  open(my $trace_report, '>', 'trace_report.txt');
  open(HIER_REPORT,"hierarchy_report.txt")||die("can't open the existing file hierarchy_report.txt ");

  struct trace => {
    file =>'$',
         module => '$',
         inst => '$',
         upSearch => '$',
         downSearch => '$',
  };

  my @trace_array;
  my $j=0;
  while(<HIER_REPORT>)
  {
    my $trace_temp=trace->new();
    $line=$_;
    if($line =~ m/File Name/)
    {
      $line=m{File Name:\s(.*)};
      $trace_file=$1;
    }
    if($line=~ m/INST/)
    {
      $line=<HIER_REPORT>;
      $line=~ m{(\S.*\s)};
      $trace_inst=$1;
    }
    if($line=~/\Wmodule/)
    {
      $line =~ m{module\s(.*\s)};
      $trace_module=$1;
    }
    if($line =~ m/\.$trace_signal\(/)
    {
      $line =~ m{\((.*)\)};
      my $upSearch=$1;
      $trace_temp->downSearch($trace_signal);
      $trace_temp->upSearch($upSearch);
      $trace_temp->file($trace_file);
      $trace_temp->inst($trace_inst);
      $trace_temp->module($trace_module);
#print $trace_report $line;
      $trace_array[$j]=$trace_temp;
      $j++;
    }
    if($line =~ m/\($trace_signal\)/)
    {
      $line=~m{\.(.*)\(};
      my $downSearch=$1;
      $trace_temp->upSearch($trace_signal);
      $trace_temp->downSearch($downSearch);
      $trace_temp->file($trace_file);
      $trace_temp->inst($trace_inst);
      $trace_temp->module($trace_module);
#print $trace_report $line;
      $trace_array[$j]=$trace_temp;
      $j++;
    }
  }
#do upsearch
print $trace_report "######### upsearch #######\n";
  $j=0;
  my $upSearch_out=0;
  $upSearch_out=upSearch(\@trace_array,\$j);

  print $trace_report "File Name: ".$trace_array[0]->file."\n";
  print $trace_report "MODULE: ".$trace_array[0]->module."\n";
  print $trace_report "INST: ".$trace_array[0]->inst."\n";
  print $trace_report "upSearch: ".$trace_array[0]->upSearch."\n";
  print $trace_report "downSearch: ".$trace_array[0]->downSearch."\n";
  print $trace_report "-----------------------------------------------------\n";
  while(1)
  {
    if($upSearch_out != -1)
    {
      print $trace_report "File Name: ".$trace_array[$upSearch_out]->file."\n";
      print $trace_report "MODULE: ".$trace_array[$upSearch_out]->module."\n";
      print $trace_report "INST: ".$trace_array[$upSearch_out]->inst."\n";
      print $trace_report "upSearch: ".$trace_array[$upSearch_out]->upSearch."\n";
      print $trace_report "downSearch: ".$trace_array[$upSearch_out]->downSearch."\n";
      print $trace_report "-----------------------------------------------------\n";
      $upSearch_out=upSearch(\@trace_array,\$upSearch_out);
    }
    else
    {
      print $trace_report "no higher level modules\n";
      last;
    }
  }
#do downsearch
print $trace_report "######### downsearch #######\n";
  $j=0;
  my $downSearch_out=0;
  $downSearch_out=downSearch(\@trace_array,\$j);
  print $trace_report "File Name: ".$trace_array[0]->file."\n";
  print $trace_report "MODULE: ".$trace_array[0]->module."\n";
  print $trace_report "INST: ".$trace_array[0]->inst."\n";
  print $trace_report "upSearch: ".$trace_array[0]->upSearch."\n";
  print $trace_report "downSearch: ".$trace_array[0]->downSearch."\n";
  print $trace_report "-----------------------------------------------------\n";
  while(1)
  {
    if($downSearch_out != -1)
    {
      print $trace_report "File Name: ".$trace_array[$downSearch_out]->file."\n";
      print $trace_report "MODULE: ".$trace_array[$downSearch_out]->module."\n";
      print $trace_report "INST: ".$trace_array[$downSearch_out]->inst."\n";
      print $trace_report "upSearch: ".$trace_array[$downSearch_out]->upSearch."\n";
      print $trace_report "downSearch: ".$trace_array[$downSearch_out]->downSearch."\n";
      print $trace_report "-----------------------------------------------------\n";
      $downSearch_out=downSearch(\@trace_array,\$downSearch_out);
    }
    else
    {
      print $trace_report "no lower level modules\n";
      last;
    }
  }
  close $trace_report;
  close HIER_REPORT;
}




#find instance that matches the current module name
sub upSearch
{
  my $in=shift;
  my $j_in=shift;
  my $j=${$j_in};
  my @in_array=@{$in};
  my $temp;
#  open(my $trace_report, '>>', 'trace_report.txt');

  my $index=0;
  while($in_array[$index])
  {
    $_=$in_array[$j]->module^$in_array[$index]->inst;
    s/./ord $& ? "^" : " "/ge;
    $temp=$_;

    if($temp !~ m/\^/)
    {
      return $index;
    }
    $index++;
  }
#  close $trace_report;
  return -1;
}





#find module with current instance name
sub downSearch
{
  my $in=shift;
  my $j_in=shift;
  my $j=${$j_in};
  my @in_array=@{$in};
  my $temp;
# open(my $trace_report, '>>', 'trace_report.txt')||die("can't open the existing file hierarchy_report.txt ");

#    print $trace_report "in downsearch\n";
  my $index=0;
  while($in_array[$index])
  {
    print $in_array[$j]->inst.$in_array[$index]->module;
    print "--------------------------------------\n";
    $_=$in_array[$j]->inst^$in_array[$index]->module;
    s/./ord $& ? "^" : " "/ge;
    $temp=$_;
    if($temp !~ m/\^/)
    {
#     close $trace_report;
      return $index;
    }
    $index++;
  }
# close $trace_report;
  return -1;
}
