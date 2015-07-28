#! /usr/bin/perl
#
use warnings;
use strict;

my $line;
my $result;
my $path;
#my $file_out;

#if($ARGV[0])
#{
#  $path=$ARGV[0];
#  chomp($line=<STDIN>);
#  print "$line\n";
#  $result = `find $path -name "*.[vc]" | xargs grep -I -r -m1 "$line" `;
#  print($result);
#}
#else
#{
#  chomp($line=<STDIN>);
  open(my $pgr, '>>', 'pgrep_report.txt');
  print $pgr "\n\n$ARGV[0]\n";
  $result = `find .  -name "*.[vc]" | xargs grep -I -r -m1 "$ARGV[0]" `;
print $pgr $result;
close $pgr;

#}

