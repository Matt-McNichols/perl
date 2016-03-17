#!/usr/bin/python

# input: list of (.py) files
# output: .txt file next to orriginal

import getopt, sys, math

# comment out nav list until make refresh_list
try:
    opts, args = getopt.getopt(sys.argv[1:], "p:m:c:")
except getopt.GetoptError as err:
    # print help information and exit:
    print str(err)
    sys.exit(2)


# define a dictionary for the different comment tags
com_tag = {'p_open':'#{',
           'p_close':'#}',
           'm_open':'%_{',
           'm_close':'%_}',
           'c_open':'//{',
           'c_close':'//}'}

# Utility functions
def grab_com(a,tag_open,tag_close):
    blk_tag = False;
    # open input file
    file_name = a;
    print file_name;
    f_in = open(file_name,'r');

    # open output file
    #   file out in exact same location as file in
    file_ex_i = file_name.rfind('.');
    file_out = file_name[:file_ex_i]+'.txt'
    f_out = open(file_out,'w');

    # loop through file_in look for open and close tags
    for line in f_in:
        # check all 4 cases of tag
        if((blk_tag==False)and((com_tag[tag_open])in line))is True:
            # previous tag was closed properly
            # line contains open tag
            f_out.write(line);
            blk_tag=True;
        elif((blk_tag==False)and((com_tag[tag_close])in line))is True:
            # no open tag has been seen but there is a close tag
            sys.exit();
        elif((blk_tag==True)and((com_tag[tag_open])in line))is True:
            # already in an open block
            # cant have another open
            sys.exit();
        elif((blk_tag==True)and((com_tag[tag_close])in line))is True:
            # block tag is coming to a close
            f_out.write(line);
            blk_tag = False;
        elif(blk_tag==True)is True:
            f_out.write(line);
    f_in.close();
    f_out.close();
    return file_out;
# ...

def str_replace(txt_name,tag_open,tag_close):
    # txt_master will hold the path for each .txt file that is created
    rep_master = {};
    in_strRep = False;
    # check for a string replace block
    # if it exists grab all string replacements
    f = open(txt_name,'r');
    for line in f:
        # check all 4 cases of tag
        if((in_strRep==False)and((com_tag[tag_open]+'$$$')in line))is True:
            # line contains open tag
            # set bool so replacement string will be added
            in_strRep=True;
        elif((in_strRep==True)and((com_tag[tag_open]+'$$$')in line))is True:
            # already in an open block
            # cant have another open
            sys.exit();
        elif((in_strRep==True)and((com_tag[tag_close])in line))is True:
            # block tag is coming to a close
            #f_out.write(line);
            in_strRep = False;
        elif(in_strRep==True)is True:
            # update the replacement dict
            # break line appart make str_orig the dict key and str_rep the dict value
            rep_idx = line.find('-->');
            str_orig = line[:rep_idx];
            str_rep = line[rep_idx:];
            print 'str_orig',str_orig;
            print 'str_rep',str_rep;

# look through each input file and copy tagged text into outupt file
for o, a in opts:
    if o in ("-p"):
        print 'python tag';
        txt_file = grab_com(a,'p_open','p_close');
    elif o in ("-m"):
        print 'matlab tag';
        txt_file = grab_com(a,'m_open','m_close');
    elif o in ("-c"):
        print 'c tag';
        txt_file = grab_com(a,'c_open','c_close');
        # do a string replace on the txt file
        str_replace(txt_file,'c_open','c_close');
