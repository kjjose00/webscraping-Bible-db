
# this code is for webscraping the whole bible from 'thiruvachanam.in' website and saving the data to a sqlite database . 


# importing the modules
from tkinter import *
import requests
from bs4 import BeautifulSoup
import sqlite3
a=Tk()
b=Text()
b.pack()
# t=int(input("enter testament('1' for old '2' for new testament):"))
booknames=['Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra','Nehemiah','Tobit','Judith','Esther','1 Maccabees','2 Maccabees','Job','Psalms','Proverbs','Ecclesiastes','Song fo songs','Wisdom','Sirach','Isaiah','Jeremiah','Lamentations','Baruch','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah','Haggai','Zecharia','Malachi','Matthew','Mark','Luke','John','Acts of Apostles','Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','Colossians','1 Thessalonians','2 Thessalonians','1 Timothy',' 2 Timoty','Titus','Philemon','Hebrews','James','1 Peter','2 Peter','1 John','2 John','3 John','Jude','Revelation']
# if (t==1):
#     for i in arr_books_old_testament:
#         print(i)
# elif (t==2):
#     for i in arr_books_new_testament:
#         print(i)
# else:
#     pass
# bk=int(input("select book number from above:"))
# chapter=int(input('enter chapter :'))

chapter_array=[51,92,120,157,192,217,239,244,276,301,324,350,380,417,428,442,457,474,497,514,530,573,724,756,769,778,798,850,917,970,976,983,1032,1047,1062,1066,1076,1078,1083,1091,1095,1099,1103,1106,1121,1126,1155,1172,1197,1219,1248,1265,1282,1296,1303,1310,1315,1320,1326,1330,1337,1342,1346,1348,1362,1368,1374,1378,1384,1386,1388,1390,1413]

# print(len(chapter_array))
chapter_length_array=[50,40,27,36,34,24,21,4,31,24,22,25,29,36,10,13,14,16,22,16,15,42,150,31,12,8,19,51,66,52,5,6,48,14,14,3,9,1,4,7,3,3,3,2,14,4,28,16,24,21,28,16,16,13,6,6,4,4,5,3,6,4,3,1,13,5,5,3,5,1,1,1,22]
# print(len(chapter_length_array))
# for i in range(1,74):
#     if (chapter<=chapter_length_array[i-1] and bk==i and bk<=46):
        
#         if (bk==1):
#             chapter=chapter
#             book=i
#             testament=1
#         else:
#             book=i
#             testament=1

#             chapter=chapter+chapter_array[i-1]
#     elif (chapter<=chapter_length_array[i-1] and bk==i and bk<=73):
#         book=i
#         chapter=chapter+chapter_array[i-1]
#         testament=2


# 
n=0

for j in range(1,74):
    for k in range(1,(chapter_length_array[j-1]+2)):
        if(j>=47):
            t=2
        else:
            t=1
        n=n+1
       
        if(n in chapter_array):
            pass
        else:

            url=f"https://thiruvachanam.in/ShowStatementsOfChapter.do?c={n}&b={j}&t={t}"
            # creating request object
            req=requests.get(url)

            # creating soup object
            data=BeautifulSoup(req.text, 'lxml')

            # finding all li tags in ul and printing the text within it
            data1=data.find('div',id='statementList')
            c=[]
            for li in data1.find_all("li"):
                c.append(li.text)
                # print(c)
            for v in c:
                con = sqlite3.connect('bible.db')
                cur = con.cursor()
                cur.execute('insert into bible values(?,?,?,?,?,?)',(t,booknames[j-1],j,k,(c.index(v))+1,v))
                con.commit()
                con.close()


                # b.insert(END,i)

            # print(len(c))

a.mainloop()

   
    

   