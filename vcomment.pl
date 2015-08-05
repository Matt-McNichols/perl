#! /usr/bin/perl
#
#use warnings;
use strict;

my $line;
my $first_line=0;

if($ARGV[0] eq 'u' or $ARGV[0] eq 'U') { # If the passed argument is u or U
  while (<STDIN>) {
    if($first_line==0){
      $line=$_;
      $first_line=1;
    }
    else{
    $line = $_;
    # Remove the begining // (i.e. uncomment line)
    $line =~ s/^\/\///;
    print($line);
    }
  }

} else {
  while (<STDIN>) {
    if($first_line==0 ){
      $line=$_;
      print"//  FIXME: $ENV{'USER'}\n//".$line;
      $first_line=1;
    }
    else{
    $line = $_;
    # Put // at the begining (i.e. comment the line out)
    print("//".$line);
    }
  }
}

