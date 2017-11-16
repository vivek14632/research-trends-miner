import os
import PyPDF2
import enchant
d = enchant.Dict("en_US")
f_no = 1

for filename in os.listdir("/Users/vijayvishwakarma/Desktop/Workspace/Test/"):
    try:
        if filename.startswith("ContentServer"):
            print(filename)
            pdf_file = open(filename, 'rb')
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            number_of_pages = read_pdf.getNumPages()
            page = read_pdf.getPage(0)
            page_content = page.extractText()

            x=page_content.split(" ")
            print(x)
            title=[]
            z=[]
            a=[]
            title.append(str(f_no))
            f_no += 1
            g = -1


            for i in range(0,len(x)):
                a = list(x[i])
                a = [" " if not(m.isalpha()) else m for m in a ]
                x[i] = ''.join(e for e in a if e.isalpha())
            x.remove('')

            '''for i in range(0, len(x)):
                if (x[i][-4:].isupper() and g == -1 and x[i+1][:4].isupper()):
                    g += i+1;'''

            if(g<0):
                g=0
            '''z=[]
            z=list(x[g])
            y=""
            for i in range(0,len(z)):
                if(''.join(z[i:]).isupper()):
                    y=''.join(z[i:])
                    break'''
            title.append(x[g])


            if(title[1].upper()=='METHODS'):
                title.append("ARTICLE")
                title.append(x[g+1][7:])
                g+=1
            elif(title[1].upper()=='THEORY'):
                title.append("AND")
                title.append("ARTICLE")
                title.append(x[g+2][7:])
                g += 1
            elif(title[1].upper()=='ISSUES'):
                title.append("AND")
                title.append("OPINIONS")
                title.append(x[g+2][8:])
                g += 1
            elif (title[1].upper() == 'SPECIAL'):
                title.append("ISSUE")
                title.append(x[g+1][5:])
                g += 1
            elif(title[1].upper()=='EDITORS'):
                title.append("COMMENTS")
                title.append(x[g+1][8:])
                g += 1
            elif (title[1].upper() == 'ERRATA'):
                title.append("NOTES")
                title.append(x[g+1][5:])
                g += 1
            elif (title[1].upper() == 'EDITORIAL'):
                title.append("INTRODUCTION")
                title.append(x[g+1][12:])
                g += 1
            elif (title[1].upper() == 'RESEARCH'):
                if(x[g+1][0].upper()=="A"):
                    title.append("ARTICLE")
                    title.append(x[g+1][7:])
                    g += 1
                if (x[g+1][0].upper() == "E"):
                    title.append("ESSAY")
                    title.append(x[g+1][5:])
                    g += 1
                if (x[g+1][0].upper()== "N"):
                    title.append("NOTE")
                    title.append(x[g+1][4:])
                    g += 1
            for i in range(len(title)+g-1,len(x)):
                if(x[i]==''):
                    continue
                if ("1" in x[i] and i>15 or "By" in x[i]):
                    break
                title.append(x[i])

            z=[]
            w=x[i]
            w = list(w)
            for j in range(0,len(w)):
                if(not(w[j].isalpha()) or (w[j]=="B" and w[j+1]=="y")):
                    break
                z.append(w[j])
            z=''.join(z)
            title.append(z)
            if (title[0] == "ERRATA" or title[0] == "EDITORS"):
                title = title[0:2]
            if (len(title)>20):
                title = title[0:20]
            title='_'.join(f for f in title if f!='')
            print(title)



            os.rename(filename, title+".pdf")

    except IndexError:
        continue