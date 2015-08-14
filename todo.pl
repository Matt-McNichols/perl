#! /usr/bin/perl
use Class::Struct;
use warnings;
use strict;


{
  struct( item => {
      name => '$',
      location => '$',
      printed => '$',
      message => '$'
      });
#global variables
  my @existing_locations;
  my $max_name=0;
  my @item_list;
  my $depth=0;
  my $file_out;
  open(my $file_out, '>', 'todo_list.md');
# main block
  {
    open( CMD_MEM, 'cmd_mem.txt')||die("cant open\n");
    while(<CMD_MEM>)
    {
      my $line=$_;
      if($line =~ m{add\((\S*)\/(\S*)\/(.*)\)})
      {
        my $temp_name = $2;
        my $temp_location =$1;
        my $temp_message=$3;

# check that location is valid
        my $return_valid=valid_location($temp_location);
        if($return_valid==0)
        {
          print"oops not a valid location";
          exit;
        }
        else
        {
          if($temp_name > $max_name)
          {
            $max_name=$temp_name;
          }

          my $temp_item=item->new();
          $temp_item->name($temp_name);
          $temp_item->location($temp_location);
          $temp_item->message($temp_message);
          $temp_item->printed(0);
          push @existing_locations, $temp_location.",".$temp_name;
          push @item_list, $temp_item;
        }
      }
      elsif($line =~ m{print})
      {
        print"ERROR";
        exit
      }
      elsif($line =~ m{del\((\S*)\/(\S*)\)})
      {
        my $del_location=$1;
        my $del_name=$2;
        for(my $i_del=0; $i_del<=$#item_list; $i_del++)
        {
          if(($item_list[$i_del]->location eq $del_location) and
              ($item_list[$i_del]->name eq $del_name))
          {
            splice @item_list, $i_del, 1;

          }
        }
      }
    }
    close CMD_MEM;
  }
  {

    open(my $cmd_mem, '>>', 'cmd_mem.txt')||die("cant open 2\n");
    while(<STDIN>)
    {
      my $line=$_;
      if($line =~ m{add\((\S*)\/(\S*)\/(.*)\)})
      {
        my $temp_name = $2;
        my $temp_location =$1;
        my $temp_message=$3;
# check that location is valid
        my $return_valid=valid_location($temp_location);
        if($return_valid==0)
        {
          print"oops not a valid location";
          exit;
        }
        else
        {
          chomp($line);
          print $cmd_mem $line.";\n";
          if($temp_name > $max_name)
          {
            $max_name=$temp_name;
          }

          my $temp_item=item->new();
          $temp_item->name($temp_name);
          $temp_item->location($temp_location);
          $temp_item->message($temp_message);
          $temp_item->printed(0);

          push @existing_locations, $temp_location.",".$temp_name;
          push @item_list, $temp_item;
        }
      }
      elsif($line =~ m{print})
      {
        my $return_print=print_tree(0);
        for(my $i_print=0; $i_print<=$#item_list; $i_print++)
        {
          $item_list[$i_print]->printed(0);
        }
        $depth=0;
        close $file_out;
      }
      elsif($line =~ m{del\((\S*)\/(\S*)\)})
      {
        my $del_location=$1;
        my $del_name=$2;
        for(my $i_del=0; $i_del<=$#item_list; $i_del++)
        {
          if(($item_list[$i_del]->location eq $del_location) and
              ($item_list[$i_del]->name eq $del_name))
          {
          chomp($line);
          print $cmd_mem $line.";\n";
            print"found item\n";
            splice @item_list, $i_del, 1;

          }
        }
      }
      elsif($line eq "q\n")
      {
        exit;
      }
    }
close $cmd_mem;
  }
#end of main block

  sub valid_location
  {
    my $temp_location=$_[0];
    if($temp_location eq '0')
    {
      return 1;
    }
    for(my $i=0; $i<=$#existing_locations; $i++)
    {
      if(($temp_location =~ m{$existing_locations[$i]}))
      {
        return 1;
      }
    }
    return 0;
  }



  sub print_tree
  {
    my $location_in=$_[0];
    if($depth==0)
    {
      `rm -f todo_list.md`;
        open($file_out, '>', 'todo_list.md');
    }
#if item has children do this
    for(my $i_name=0; $i_name<=$max_name; $i_name++)
    {
      for(my $i_item=0; $i_item<=$#item_list; $i_item++)
      {
        if(($item_list[$i_item]->location eq $location_in)and
            ($item_list[$i_item]->name eq $i_name)and
            ($item_list[$i_item]->printed==0)
          )
        {
          my $print_string= "\* \<".$item_list[$i_item]->location.",".$item_list[$i_item]->name."\>---  ".$item_list[$i_item]->message."\n";
          for(my $i_depth=0; $i_depth<$depth; $i_depth++)
          {
            $print_string = "\t".$print_string;
          }
          if($depth==0)
          {
            print $file_out "\n---\n";
          print $file_out $print_string;
          print $print_string;
          $item_list[$i_item]->printed(1);
          }
          else
          {
          print $file_out $print_string;
          print $print_string;
          $item_list[$i_item]->printed(1);
          }
          $depth++;
          my $return_print=print_tree($item_list[$i_item]->location.",".$item_list[$i_item]->name);
        }
      }
    }
    $depth--;
    return 0;
  }

      close $file_out;
}
#end of global
