#! /usr/bin/perl
use Class::Struct;
use warnings;
use strict;

struct( item => {
    name => '$',
    location => '@',
    });

my @outputs;
my $line;
my @todoList;

while(<STDIN>)
{
  $line=$_;
  if($line =~ m{addItem\((\S*)\s(\S*)\)})
  {
    my $check_valid=valid_locations($1);
    if($check_valid==-2)
    {
      print "non-valid location entered\n";
      exit;
    }
    my @location_array=split(',',$1);
    my $new_item=item->new();
    $new_item->name($2);
    my $i=0;
    while($location_array[$i])
    {
      $new_item->location($i,$location_array[$i]);
      $i++;
    }
    push @todoList, $new_item;

  }
  elsif($line =~ m{print})
  {
    my $print_return=sort_locations(\@todoList)
  }
  else
  {
    print "that didnt work\n";
  }
#call sub that prints the name based on the location

}


sub sort_locations
{
  my $in=shift;
  my @in_array=@{$in};
  my $temp_item=item->new();

#sort array by location array size
  for(my $i=0; $i<$#in_array; $i++)
  {
    for(my $j=0; $j<($#in_array-$i); $j++)
    {
      for(my $k=0; $k<$#in_array; $k++)
      {
        if(($#{$in_array[$j]->location}>=$k)&&($#{$in_array[$j+1]->location}>=$k))
        {
        if(${$in_array[$j]->location}[$k] > ${$in_array[$j+1]->location}[$k])
        {
          $temp_item=$in_array[$j];
          $in_array[$j]=$in_array[$j+1];
          $in_array[$j+1]=$temp_item;
        }
        }
      }
    }
  }
#sort by value within same size
  my $return_print=print_list(\@in_array);
  return 0;
}



sub print_list
{
  my $in = shift;
  my @in_array=@{$in};
  for(my $k=0; $k<=$#in_array; $k++)
  {
    my $array_string=join(',',@{$in_array[$k]->location});
    my $temp_out= $array_string."---".$in_array[$k]->name."\n";
    for(my $i=0; $i<=$#{$in_array[$k]->location}; $i++)
    {
      $temp_out="\t".$temp_out;
    }
    push @outputs, $temp_out;
  }
  my $i=0;
  for($i=0; $i<=$#outputs; $i++)
  {
    print $outputs[$i];
  }
  return 0;
}







sub valid_locations
{
  my $new=$_[0];
my @existing_locations;
#check for valid locations
#if location is not valid throw it out
  if($new !~ m{,})
  {
    push @existing_locations, $new;
    return 0;
  }
  else
  {
    for(my $i=0; $i<=$#existing_locations; $i++)
    {
#why dont i ever go in here?????
      print $new;
      print $existing_locations[$i];
        if($new =~m{ $existing_locations[$i]} )
        {
          push @existing_locations, $new;
          return 0;
        }
    }
  }
  return -2;
}
