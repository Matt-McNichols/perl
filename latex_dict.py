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




    def c2tex(self,file_name):
        self.tex(file_name,self.com['c_com'],self.com_tag['c_open'],self.com_tag['c_close']);
        return;

    def py2tex(self,file_name):
        self.tex(file_name,self.com['p_com'],self.com_tag['p_open'],self.com_tag['p_close']);
        return;


    def mat2tex(self,file_name):
        self.tex(file_name,self.com['m_com'],self.com_tag['m_open'],self.com_tag['m_close']);
        return;



# define utility functions
    def tex(self,file_name,com_in,tag_open,tag_close):
#        print 'file Name: ',file_name;
#        print 'com_in: ',com_in;
#        print 'tag_open',tag_open;
#        print 'tag_close',tag_close;
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

'''

        # add lines of the file to section called file text
        verbatim = False;
        for line in f_in:
            com_off = len(com_in);
            com_tag_off = len(tag_open);
            # check verbatim status
            if((verbatim == False)and(("begin{verbatim}")in line))is True:
                com_idx = line.find(com_in);
                line = line[(com_idx+com_off):];
                verbatim=True;
            if((verbatim == True)and(("end{verbatim}")in line))is True:
                verbatim=False;

            # look for special latex commands
            # check for subsections
            if (tag_open)in line:
                subsection = '\n\\section{'+line[com_tag_off:].strip()+'}\n';
                file_text = file_text + subsection;
            else:
                # write as a latex line if there are more than 2 chars
                if((tag_close not in line )and (verbatim==False)) is True:
                    comment_idx = line.find(com_in);
                    file_text=  file_text + line[(comment_idx+com_off):];
                elif(verbatim ==True)is True:
                    file_text= file_text+line;

        # write all of the file text at once
        self.f_out.write(file_text);
    #...
