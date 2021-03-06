# print help information and exit:
        print str(err)
        sys.exit(2)



    title_bool = False;
    f_out_bool = False;

    # write the latex file header
    header= '''
\\documentclass{report}
\usepackage{geometry}
\usepackage[dvipsnames]{xcolor}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{float}
\usepackage{amsmath}
\usepackage{subcaption}
\usepackage{caption}
\usepackage{mathtools}
\usepackage{todonotes}
\usepackage{listings}

\graphicspath{ {images/}}
\hypersetup{
colorlinks=true,
linktoc=all,
linkcolor=blue!60,
}
\\geometry{legalpaper, portrait, margin=0.5in}
\\lstdefinestyle{custom}{
  basicstyle=\\small\\ttfamily,
  columns=flexible,
  breaklines=true,
  frame=single,
  language= ,
  keepspaces=true,
  backgroundcolor=\\color{gray!20},
  keywordstyle=\\bfseries\\color{purple!70!black},
  identifierstyle=\color{black},
  stringstyle=\color{orange},
  commentstyle=\\color{green!40!black}
}

\\lstset{style=custom}

\\title{Default Title}
\\author{Matt McNichols}
\\date{\\today}

\\DeclarePairedDelimiter\\floor{\\lfloor}{\\rfloor}



\\begin{document}
\\maketitle
\\tableofcontents
\\listoffigures
'''
    main_file=None;
    f_out = None;



    # look through each input file and make it a chapter
    for o, a in opts:
        # tags for setting up the output file
        if((("-t") in o) and (title_bool==False))is True:
        # -t stands for title
            title = a.replace('_',' ');
            header = header.replace('Default Title',title);

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
