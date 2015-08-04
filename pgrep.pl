#! /usr/bin/perl
use warnings;
use strict;

my $line;
my $result;
my $path;

open(my $pgr, '>>', 'pgrep_report.txt');
print $pgr "\n\n-->$ARGV[0]\n";
$result = `find .  -name "*.[vc]" | xargs grep -I -r -m1 "$ARGV[0]" `;
print $pgr $result;
close $pgr;


