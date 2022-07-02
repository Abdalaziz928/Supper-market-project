from tkinter import  *
from tkinter import messagebox
import webbrowser
import os 
import sys
pro = Tk()
pro.geometry('800x450+280+50')

pro.resizable(False,False)

pro.title('SuperMarket')

title = Label(pro,text ="Super Market System",fg='gold',bg = 'black',font =('tajawal',16,'bold'))
title.pack(fill = X)
u1 = 'https://ar-ar.facebook.com/'
u2 = 'https://twitter.com/?lang=ar'
u3 = 'https://www.youtube.com/watch?v=XaqMG7h2kuU'

def Open1():
    webbrowser.open_new(u1)

def Open2():
    webbrowser.open_new(u2)

def Open3():
    webbrowser.open_new(u3)

def about1():
    messagebox.showinfo("المطور ","عبدالعزيز")

def about2():
    messagebox.showinfo('لمحة عن المشروع',' مشروع سوبر ماركت')

def log():
    user = En1.get()
    passw = En2.get()
    if user == 'Admin' and passw == '123456':
        messagebox.showinfo('ترحيب ','اهلا بك بيانات صحيحة')

    else:
        messagebox.showinfo('خطا',' للاسف البيانات خاطئة')






F1 = Frame(pro,width = 230,height =450,bg = '#0B2F3A' )
F1.place(x= 570,y=37)
Title1 = Label(F1,text = 'مشروع سوبر ماركت',fg = 'white',bg = '#0B2F3A',font =('tagawal',14,'bold'))
Title1.place(x=50, y = 10)
Title2 = Label(F1,text = 'المطور عبدالعزيز دياب',bg = '#0B2F3A',fg = 'white',font =('tagawal',12,'bold'))
Title2.place(x = 50,y = 50)
Title3 = Label(F1,text ='وسائل الاتصال بنا',fg = 'white',bg = '#DBA901',font =('tagawal',12,'bold'))
Title3.place(x = 65,y =90)
B1 = Button(F1,text = 'حسابناعلي الفيس بوك',width = 26,fg = 'black',bg = '#DBA901',font= ('tagawal',12,'bold'),command = Open1)
B1.place(x = 4,y = 130)
B1 = Button(F1,text = 'حسابنا علي تويتر',width = 26,fg = 'black',bg = '#DBA901',font= ('tagawal',12,'bold'),command = Open2)
B1.place(x = 4,y = 177)
B1 = Button(F1,text ='قناتنا علي اليوتيوب',width = 26,fg = 'black',bg = '#DBA901',font= ('tagawal',12,'bold'),command = Open3)
B1.place(x = 4,y = 225)
B1 = Button(F1,text = 'لمحة عن المطور',width = 26,fg = 'black',bg = '#DBA901',font= ('tagawal',12,'bold'),command = about1)
B1.place(x = 4,y = 277)
B1 = Button(F1,text = 'لمحة عن المشروع',width = 26,fg = 'black',bg = '#DBA901',font= ('tagawal',12,'bold'),command = about2)
B1.place(x = 4,y = 318)
B1 = Button(F1,text = 'الخروج من البرنامج',width = 26,fg = 'black',bg = '#DBA901',font= ('tagawal',12,'bold'),command =quit)
B1.place(x = 4,y = 365)
photo = PhotoImage(file='SuPer.png')
imo = Label(pro,image = photo)
imo.place(x = 150, y = 75,width =308,height = 272 )


F2 = Frame(pro , width = 570,height = 120,bg = '#0B2F3A')
F2.place(x = 0,y = 330)
photo1 = PhotoImage(file ='logee.png' )
imo1 = Label(pro,image = photo1)
imo1.place(x= 450,y = 335,width=110,height= 110)
L1 = Label(F2,text = 'اسم المستخدم',fg = 'gold',bg ='#0B2F3A',font = ('tajawal','14','bold'))
L1.place( x= 330, y=25)
L2 = Label(F2,text = 'كلمة المرور',fg = 'gold',bg ='#0B2F3A',font = ('tajawal','14','bold'))
L2.place( x= 330, y=70)
En1 = Entry(F2, font = ('tajawal',12),justify='center')
En1.place(x = 130,y = 26)
En2 = Entry(F2, font = ('tajawal',12),justify='center')
En2.place(x = 130,y = 71)
B = Button(F2 , text = 'تسجيل الدخول',bg = '#DBA901',font = ('tajawal',12),width = 12, height = 3,command = log)
B.place( x = 10,y = 20)
pro.mainloop()


