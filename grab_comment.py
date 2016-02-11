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

# look through each input file and copy tagged text into outupt file
for o, a in opts:
    if o in ("-p"):
        print 'python tag';
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
            if((blk_tag==False)and((com_tag['p_open'])in line))is True:
                # previous tag was closed properly
                # line contains open tag
                f_out.write(line);
                blk_tag=True;
            elif((blk_tag==False)and((com_tag['p_close'])in line))is True:
                # no open tag has been seen but there is a close tag
                sys.exit();
            elif((blk_tag==True)and((com_tag['p_open'])in line))is True:
                # already in an open block
                # cant have another open
                sys.exit();
            elif((blk_tag==True)and((com_tag['p_close'])in line))is True:
                # block tag is coming to a close
                f_out.write(line);
                blk_tag = False;
            elif(blk_tag==True)is True:
                f_out.write(line);
    elif o in ("-m"):
        print 'matlab tag';
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
            if((blk_tag==False)and((com_tag['m_open'])in line))is True:
                # previous tag was closed properly
                # line contains open tag
                f_out.write(line);
                blk_tag=True;
            elif((blk_tag==False)and((com_tag['m_close'])in line))is True:
                # no open tag has been seen but there is a close tag
                sys.exit();
            elif((blk_tag==True)and((com_tag['m_open'])in line))is True:
                # already in an open block
                # cant have another open
                sys.exit();
            elif((blk_tag==True)and((com_tag['m_close'])in line))is True:
                # block tag is coming to a close
                f_out.write(line);
                blk_tag = False;
            elif(blk_tag==True)is True:
                f_out.write(line);
    elif o in ("-c"):
        print 'c tag';
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
            if((blk_tag==False)and((com_tag['c_open'])in line))is True:
                # previous tag was closed properly
                # line contains open tag
                f_out.write(line);
                blk_tag=True;
            elif((blk_tag==False)and((com_tag['c_close'])in line))is True:
                # no open tag has been seen but there is a close tag
                sys.exit();
            elif((blk_tag==True)and((com_tag['c_open'])in line))is True:
                # already in an open block
                # cant have another open
                sys.exit();
            elif((blk_tag==True)and((com_tag['c_close'])in line))is True:
                # block tag is coming to a close
                f_out.write(line);
                blk_tag = False;
            elif(blk_tag==True)is True:
                f_out.write(line);
