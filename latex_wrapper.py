#!/usr/bin/python

# input: list of input .txt file
# output: .tex file

# FIXME: make into class
# define utility functions
def c2tex(file_name):
    f_in = open(file_name,'r');

    #  chapter name
    t_front = file_name.rfind('/');
    t_back = file_name.rfind('.');

    name = file_name[(t_front+1):t_back]
    #replace '_' with '
    name = name.replace("_"," ");
    # make a new chapter for the file
    file_text = '''
\\chapter{'''+name+'''}
This is where you will describe the document as a whole

\\section{File Text}
'''

    # add lines of the file to section called file text
    verbatim = False;
    for line in f_in:
        com_off = len(com['c_com']);
        com_tag_off = len(com_tag['c_open']);
        # check verbatim status
        if((verbatim == False)and(("begin{verbatim}")in line))is True:
            com_idx = line.find(com['c_com']);
            line = line[(com_idx+com_off):];
            verbatim=True;
        if((verbatim == True)and(("end{verbatim}")in line))is True:
            verbatim=False;

        # look for special latex commands
        # check for subsections
        if (com_tag['c_open'])in line:
            subsection = '\n\\subsection{'+line[com_tag_off:].strip()+'}\n';
            file_text = file_text + subsection;
        # check for \href links
        elif ('\\href')in line:
            file_text = file_text+line;
        else:
            # write as a latex line if there are more than 2 chars
            if((com_tag['c_close'] not in line )and (verbatim==False)) is True:
                comment_idx = line.find(com['c_com']);
                file_text=  file_text + line[(comment_idx+com_off):];
            elif(verbatim ==True)is True:
                file_text= file_text+line;

    # end of section close verbatim
#file_text=file_text+'\\end{verbatim}\n';
    f_out.write(file_text);


def mat2tex(file_name):
    f_in = open(file_name,'r');

    #  chapter name
    t_front = file_name.rfind('/');
    t_back = file_name.rfind('.');

    name = file_name[(t_front+1):t_back]
    #replace '_' with '
    name = name.replace("_"," ");
    # make a new chapter for the file
    file_text = '''
\\chapter{'''+name+'''}
This is where you will describe the document as a whole

\\section{File Text}
'''

    # add lines of the file to section called file text
    verbatim = False;
    for line in f_in:
        # check verbatim status
        if((verbatim == False)and(("begin{verbatim}")in line))is True:
            pound = line.find(com['m_com']);
            line = line[(pound+1):];
            verbatim=True;
        if((verbatim == True)and(("end{verbatim}")in line))is True:
            verbatim=False;

        # check for subsections
        if (com_tag['m_open'])in line:
            first = len(com_tag['m_open']);
            subsection = '\n\\subsection{'+line[first:].strip()+'}\n';
            file_text = file_text + subsection;
        # check for \href links
        elif ('\\href')in line:
            file_text = file_text+line;
        else:
            # write as a latex line if there are more than 2 chars
            if((com_tag['m_close'] not in line )and (verbatim==False)) is True:
                comment_idx = line.find(com['m_com']);
                file_text=  file_text + line[(comment_idx+1):];
            elif(verbatim ==True)is True:
                file_text= file_text+line;

    # end of section close verbatim
#file_text=file_text+'\\end{verbatim}\n';
    f_out.write(file_text);















# Start of script
import getopt, sys, math

# comment out nav list until make refresh_list
try:
    opts, args = getopt.getopt(sys.argv[1:], "p:m:o:t:c:")

except getopt.GetoptError as err:
    # print help information and exit:
    print str(err)
    sys.exit(2)

# open output file
#   file out in exact same location as file in
#file_ex_i = file_name.rfind('.');
#file_out = file_name[:file_ex_i]+'.tex'

# define a dictionary for different comment types
com = {'p_com':'#','m_com':'%','c_com':'//'};
com_tag = {'p_open':'#{','p_close':'#}','m_open':'%_{','m_close':'%_}','c_open':'//{','c_close':'//}'}

title_bool = False;
f_out_bool = False;

# write the latex file header
header= '''
\\documentclass{report}
\usepackage{geometry}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{float}
\usepackage{amsmath}
\usepackage{subcaption}
\usepackage{caption}
%\usepackage{todonotes}


\graphicspath{ {images/}}
\hypersetup{
colorlinks=true,
linktoc=all,
linkcolor=blue!60,
}
\\geometry{legalpaper, portrait, margin=0.5in}
\\title{Default Title}
\\author{Matt McNichols}
\\date{February 4, 2016}

\\begin{document}
\\maketitle
\\tableofcontents
'''
main_file=None;
f_out = None;



# look through each input file and make it a chapter
for o, a in opts:
    if((("-t") in o) and (title_bool==False))is True:
    # -t stands for title
        header= '''
        \\documentclass{report}
        \usepackage{geometry}
        \usepackage{xcolor}
        \usepackage{hyperref}
        \usepackage{graphicx}
        \usepackage{float}
        \usepackage{amsmath}
        \usepackage{subcaption}
        \usepackage{caption}
        %\usepackage{todonotes}

        \graphicspath{ {images/}}
        \hypersetup{
          colorlinks=true,
          linktoc=all,
          linkcolor=blue!60,
        }
        \\geometry{legalpaper, portrait, margin=0.5in}
        \\title{'''+a.replace('_',' ')+'''}
        \\author{Matt McNichols}
        \\date{February 4, 2016}

        \\begin{document}
        \\maketitle
        \\tableofcontents
        '''
    elif((("-t") in o) and (title_bool==True))is True:
            print 'Error: title already given';
            sys.exit(2);

    if("-o") in o:
        if f_out_bool is True:
            print 'Error: f_out already given';
            sys.exit(2);
        else:
            f_out_bool = True;
            file_out = a;
            f_out = open(file_out,'w');
            f_out.write(header);
    if ("-p")in o:
        if f_out_bool is False:
            print 'Error: f_out not assigned';
            sys.exit(2);
#        print(["flag", o],1);
#        print(["args", a],1);
        file_name = a;


        f_in = open(file_name,'r');

        #  chapter name
        t_front = file_name.rfind('/');
        t_back = file_name.rfind('.');

        name = file_name[(t_front+1):t_back]
        #replace '_' with '
        name = name.replace("_"," ");
        # make a new chapter for the file
        file_text = '''
\\chapter{'''+name+'''}
This is where you will describe the document as a whole

\\section{File Text}
'''

        # add lines of the file to section called file text
        verbatim = False;
        for line in f_in:
            # check verbatim status
            if((verbatim == False)and(("begin{verbatim}")in line))is True:
                pound = line.find(com['p_com']);
                line = line[(pound+1):];
                verbatim=True;
            if((verbatim == True)and(("end{verbatim}")in line))is True:
                verbatim=False;

            # check for subsections
            if (com_tag['p_open'])in line:
                subsection = '\n\\subsection{'+line[2:].strip()+'}\n';
                file_text = file_text + subsection;
            # check for \href links
            elif ('\\href')in line:
                file_text = file_text+line;
            else:
                # write as a math line if there are more than 2 chars
                if((com_tag['p_close'] not in line )and (verbatim==False)) is True:
                    comment_idx = line.find(com['p_com']);
                    file_text=  file_text + line[(comment_idx+1):];
                elif(verbatim ==True)is True:
                    file_text= file_text+line;

        # end of section close verbatim
#file_text=file_text+'\\end{verbatim}\n';
        f_out.write(file_text);
    #...
    elif ("-m")in o:
#        print(["flag", o],1);
#        print(["args", a],1);

        # put main file first in the document
        # put images under each figure call in main
        # put the function files under the main file
        if (("main")in a)is True:
            print 'file name: ', a
            main_file = a;
            mat2tex(main_file);
        else:
            print 'file name: ', a
            file_name = a;
            mat2tex(file_name);
    elif("-c") in o:
        file_name = a;
        c2tex(file_name);



# end file document
f_out.write('\\end{document}');
