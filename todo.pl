#! /usr/bin/perl
use Class::Struct;
use warnings;
use strict;


#global variables
{
  struct( item => {
      name => '$',
      location => '$',
      printed => '$',
      print_valid => '$',
      message => '$'
      });

#  my @existing_locations;
  my $max_name=0;
  my @item_list;
  my $depth=0;

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
#     my $return_valid=valid_location($temp_location,$temp_name);
#       if($return_valid==0)
#       {
#         print"oops not a valid location";
#         exit;
#       }
#       elsif($return_valid==1)
#       {
          chomp($line);
          if($temp_name > $max_name)
          {
            $max_name=$temp_name;
          }

          my $temp_item=item->new();
          $temp_item->name($temp_name);
          $temp_item->location($temp_location);
          $temp_item->message($temp_message);
          $temp_item->print_valid(1);
          $temp_item->printed(0);

#          push @existing_locations, $temp_location.",".$temp_name;
          push @item_list, $temp_item;
#       }
#       elsif($return_valid==2)
#       {
#         print "edited existing item\n";
#         my $check=0;
#         for(my $i_edit=0; $i_edit<=$#item_list; $i_edit++)
#         {
#           if(($temp_location eq $item_list[$i_edit]->location)and($temp_name eq $item_list[$i_edit]->name))
#           {
#             $item_list[$i_edit]->message($temp_message);
#             $check=1;
#           }
#         }
#         if($check eq 0)
#         {
#           print "Error item_list and existing_locations do not match\n";
#           exit;
#         }
#       }
      }
      elsif($line =~ m{print})
      {
        print"ERROR\n";
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
            $item_list[$i_del]->print_valid(0);

          }
        }
      }
    }
    close CMD_MEM;
  }
  {

    open(my $cmd_mem, '>>', 'cmd_mem.txt')||die("cant open 2\n");
#If there are items in the list print them at the start of the program
      if($#item_list>=0)
      {
        my $return_print=print_tree(0);
        for(my $i_print=0; $i_print<=$#item_list; $i_print++)
        {
          $item_list[$i_print]->printed(0);
        }
        $depth=0;
        close $file_out;
      }
    while(<STDIN>)
    {
      print"======================================\n";
      my $line=$_;
      if($line =~ m{add\((\S*)\/(\S*)\/(.*)\)})
      {
        my $temp_name = $2;
        my $temp_location =$1;
        my $temp_message=$3;
# check that location is valid
        my $return_valid=valid_location($temp_location,$temp_name);
        print $return_valid;
        if($return_valid==0)
        {
          print"oops not a valid location\n";
          exit;
        }
        elsif($return_valid==1)
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
          $temp_item->print_valid(1);
#add print valid bit set to true
#          push @existing_locations, $temp_location.",".$temp_name;
          push @item_list, $temp_item;
        }
        elsif($return_valid==2)
        {
          print "edited existing item\n";
          my $check=0;
          for(my $i_edit=0; $i_edit<=$#item_list; $i_edit++)
          {
            if(($temp_location eq $item_list[$i_edit]->location)and($temp_name eq $item_list[$i_edit]->name))
            {
              $item_list[$i_edit]->message($temp_message);
              $item_list[$i_edit]->print_valid(1);
          print $cmd_mem "add(".$item_list[$i_edit]->location."\/".$item_list[$i_edit]->name."\/".$item_list[$i_edit]->message.");\n";
              $check=1;
            }
          }
          if($check eq 0)
          {
            print "Error item_list and existing_locations do not match\n";
            exit;
          }
        }
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
#instead of splice just set a print valid bit to false
            $item_list[$i_del]->print_valid(0);

          }
        }
      }
      elsif($line eq "q\n")
      {
        exit;
      }
      if($#item_list>=0)
      {
        my $return_print=print_tree(0);
        for(my $i_print=0; $i_print<=$#item_list; $i_print++)
        {
          $item_list[$i_print]->printed(0);
        }
        $depth=0;
        close $file_out;
      }
    }
    close $cmd_mem;
  }
#end of main block

  sub valid_location
  {
    my $temp_location=$_[0];
    my $temp_name=$_[1];
    my $return_val=0;
    for(my $i=0; $i<=$#item_list; $i++)
    {
#convert to item list
      if(($temp_location eq $item_list[$i]->location) and ($temp_name eq $item_list[$i]->name))
      {
        print "location already exists\n";
        $return_val=2;
        return $return_val;
      }
      elsif($temp_location eq $item_list[$i]->location.','.$item_list[$i]->name)
      {
        $return_val= 1;
      }
    }
    if($temp_location eq '0')
    {
      return 1;
    }
    return $return_val;
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
            ($item_list[$i_item]->printed eq 0)and
            ($item_list[$i_item]->print_valid == 1)
          )
        {
          my $print_string= "\* \<".$item_list[$i_item]->location.",".$item_list[$i_item]->name."\>---  ".$item_list[$i_item]->message."\n";
          my $print_md_string= "\*   ".$item_list[$i_item]->message."\n";
          for(my $i_depth=0; $i_depth<$depth; $i_depth++)
          {
            $print_string = "\t".$print_string;
            $print_md_string = "\t".$print_md_string;
          }
          if($depth==0)
          {
            print $file_out "\n---\n";
          print $file_out $print_md_string;
          print $print_string;
          $item_list[$i_item]->printed(1);
          }
          else
          {
          print $file_out $print_md_string;
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
