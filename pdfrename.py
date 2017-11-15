import os
import PyPDF2
import enchant
d = enchant.Dict("en_US")
for filename in os.listdir("/Users/vijayvishwakarma/Desktop/Workspace/Test/"):
    if filename.startswith("ContentServer"):
        print(filename)
        pdf_file = open(filename, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)
        x=page_content.split(" ")
        #print(x)
        #print(x[1][7:])
        title=[]
        z=[]
        #print(x[1])
        a=[]
        #print(x)
        for i in range(0,len(x)):
            a = list(x[i])
            a = ''.join(e for e in a if e.isalnum())
            x[i] = ''.join(a)
        #print(x)
        '''for i in range(0,20):
            a = list(x[i])
            b = []
            if(not(d.check(x[i]))):
                print(x[i],not(d.check(x[i])))
                for n in range(3,len(a)):
                    b=a[n:]

                    if (d.check(''.join(b))):
                        x[i]=''.join(b)
                        x.insert(i,''.join(a[:n]))
                        print(''.join(b),''.join(a[n:]))'''
        title.append(x[0])
        if(x[0]=='METHODS'):
            title.append("ARTICLE")
            title.append(x[1][7:])
        elif(x[0]=='THEORY'):
            title.append(x[1])
            title.append(x[2][:6])
            title.append(x[2][6:])
        elif(x[0]=='ISSUES'):
            title.append(x[1])
            title.append(x[2][:8])
            title.append(x[2][9:])
        elif (x[0] == 'SPECIAL'):
            title.append(x[1][:7])
            title.append(x[1][7:])
        elif(x[0]=='EDITOR™S'):
            title.append(x[1][:8])
            title.append(x[1][8:])

        name_length=10;

        for i in range(len(title),name_length):
            if(not(x[i].isalpha()) and x[i].isalnum()):
                break
            if(x[i]==''):
                continue
            title.append(x[i])

        w=x[i]
        w = list(w)
        #print(w)
        for j in range(0,len(w)):
            if(not(w[j].isalpha())):
                break
            z.append(w[j])
            #print(z)
        z=''.join(z)
        #print(z)
        title.append(z)
        #print(title)
        #''.join(e for e in string if e.isalnum())
        #title='_'.join(e for e in title if e.isalnum())
        title='_'.join(f for f in title if f!='' and f.isupper())
        print(title)


        #os.rename(filename, title+".pdf")