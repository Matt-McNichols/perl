#!/usr/bin/python

# input: list of input .txt file
# output: .tex file

# FIXME: make into class



# Start of script
import getopt, sys, math
from latex_dict import latex_wrapper

def main():
    # comment out nav list until make refresh_list
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:m:o:t:c:")

    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)
        sys.exit(2)



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
\\date{\\today}

\\begin{document}
\\maketitle
\\tableofcontents
'''
    main_file=None;
    f_out = None;



    # look through each input file and make it a chapter
    for o, a in opts:
        # tags for setting up the output file
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
\\date{\\today}

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
                # only once we have an output file
                # do we make an instance of latex wrapper class
                LW = latex_wrapper(file_out,header);


        # tags for adding files to output files
        if ("-p")in o:
            if f_out_bool is False:
                print 'Error: f_out not assigned';
                sys.exit(2);
#        print(["flag", o],1);
#        print(["args", a],1);
            file_name = a;
            LW.py2tex(file_name);


        elif ("-m")in o:
#        print(["flag", o],1);
#        print(["args", a],1);

            # put main file first in the document
            # put images under each figure call in main
            # put the function files under the main file
            if (("main")in a)is True:
                print 'file name: ', a
                main_file = a;
                LW.mat2tex(main_file);
            else:
                print 'file name: ', a
                file_name = a;
                LW.mat2tex(file_name);
        elif("-c") in o:
            file_name = a;
            LW.c2tex(file_name);



    # end file document
    LW.f_out.write('\\end{document}');


if __name__ == '__main__':
    main()
