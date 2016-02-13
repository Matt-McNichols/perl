#!/usr/bin/python


# tab is 4 spaces in this doc

class latex_wrapper(object):

    def __init__(self,file_out,header):
        # define a dictionary for different comment types
        self.com = {'p_com':'#','m_com':'%','c_com':'//'};
        self.com_tag = {'p_open':'#{','p_close':'#}','m_open':'%_{','m_close':'%_}','c_open':'//{','c_close':'//}'}
        self.f_out = open(file_out,'w');
        self.f_out.write(header);
    #...


    # define utility functions
    def c2tex(self,file_name):
        f_in = open(file_name,'r');

        #  chapter name
        t_front = file_name.rfind('/');
        t_back = file_name.rfind('.');

        name = file_name[(t_front+1):t_back]
        # replace '_' with '
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
            com_off = len(self.com['c_com']);
            com_tag_off = len(self.com_tag['c_open']);
            # check verbatim status
            if((verbatim == False)and(("begin{verbatim}")in line))is True:
                com_idx = line.find(self.com['c_com']);
                line = line[(com_idx+com_off):];
                verbatim=True;
            if((verbatim == True)and(("end{verbatim}")in line))is True:
                verbatim=False;

            # look for special latex commands
            # check for subsections
            if (self.com_tag['c_open'])in line:
                subsection = '\n\\subsection{'+line[com_tag_off:].strip()+'}\n';
                file_text = file_text + subsection;
            # check for \href links
            elif ('\\href')in line:
                file_text = file_text+line;
            else:
                # write as a latex line if there are more than 2 chars
                if((self.com_tag['c_close'] not in line )and (verbatim==False)) is True:
                    comment_idx = line.find(self.com['c_com']);
                    file_text=  file_text + line[(comment_idx+com_off):];
                elif(verbatim ==True)is True:
                    file_text= file_text+line;

        # write all of the file text at once
        self.f_out.write(file_text);
    #...


    # define utility functions
    def py2tex(self,file_name):
        f_in = open(file_name,'r');

        #  chapter name
        t_front = file_name.rfind('/');
        t_back = file_name.rfind('.');

        name = file_name[(t_front+1):t_back]
        # replace '_' with '
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
            com_off = len(self.com['p_com']);
            com_tag_off = len(self.com_tag['p_open']);
            # check verbatim status
            if((verbatim == False)and(("begin{verbatim}")in line))is True:
                com_idx = line.find(self.com['p_com']);
                line = line[(com_idx+com_off):];
                verbatim=True;
            if((verbatim == True)and(("end{verbatim}")in line))is True:
                verbatim=False;

            # look for special latex commands
            # check for subsections
            if (self.com_tag['p_open'])in line:
                subsection = '\n\\subsection{'+line[com_tag_off:].strip()+'}\n';
                file_text = file_text + subsection;
            # check for \href links
            elif ('\\href')in line:
                file_text = file_text+line;
            else:
                # write as a latex line if there are more than 2 chars
                if((self.com_tag['p_close'] not in line )and (verbatim==False)) is True:
                    comment_idx = line.find(self.com['p_com']);
                    file_text=  file_text + line[(comment_idx+com_off):];
                elif(verbatim ==True)is True:
                    file_text= file_text+line;

        # write all of the file text at once
        self.f_out.write(file_text);
    #...




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
                pound = line.find(self.com['m_com']);
                line = line[(pound+1):];
                verbatim=True;
            if((verbatim == True)and(("end{verbatim}")in line))is True:
                verbatim=False;

            # check for subsections
            if (self.com_tag['m_open'])in line:
                first = len(self.com_tag['m_open']);
                subsection = '\n\\subsection{'+line[first:].strip()+'}\n';
                file_text = file_text + subsection;
            # check for \href links
            elif ('\\href')in line:
                file_text = file_text+line;
            else:
                # write as a latex line if there are more than 2 chars
                if((self.com_tag['m_close'] not in line )and (verbatim==False)) is True:
                    comment_idx = line.find(self.com['m_com']);
                    file_text=  file_text + line[(comment_idx+1):];
                elif(verbatim ==True)is True:
                    file_text= file_text+line;

        # write all of the file text at once
        self.f_out.write(file_text);
    #...
