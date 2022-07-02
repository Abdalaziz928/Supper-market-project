from tkinter import *
import math , random,os

from tkinter import messagebox
class Super:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1300x700+30+10')
        self.root.title('Supermarket')
        self.root.resizable(False,False)
        self.root.iconbitmap('D:\\icon.jpg')
        title = Label(self.root,text = 'ادارة المشاريع: سوبر ماركت',fg = "white",bg = '#0B2F3A',font = ('tajawal',15))
        title.pack(fill = X)
        # ===  المتغيرات
        # القوليات
        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()
        self.q4 = IntVar()
        self.q5 = IntVar()
        self.q6 = IntVar()
        self.q7 = IntVar()
        self.q8 = IntVar()
        self.q9 = IntVar()
        self.q10 = IntVar()
        self.q11 = IntVar()


        # === متغيرات بيانات المشتري
        self.name = StringVar()
        self.phone = StringVar()
        self.number = StringVar()
        x = random.randint(1000,9999 )
        self.number.set(str(x))

        # =====  متغيرات الحساب الكلي=======

        self.bocoliat = StringVar()
        self.adoat = StringVar()
        self.kahraba = StringVar ()
        

        # بيانات المستخدم
        F1 = Frame(root,bd = 2,width = 338, height = 170,bg = '#0B2F3A')
        F1.place(x = 961,y = 35)
        tit = Label(F1,text = ':بيانات المشتري',font = ('tajawal',13,'bold'),bg = '#0B2F3A',fg = 'tomato')
        tit.place(x = 185,y =0)
        his_name = Label(F1,text = 'اسم المشتري',font = ('tajawal',10),bg = '#0B2F3A',fg = 'gold')
        his_name.place(x = 230,y=40)
        his_phone = Label(F1,text = 'رقم الهاتف',font = ('tajawal',10),bg = '#0B2F3A',fg = 'gold')
        his_phone.place(x = 235,y=70)
        his_num = Label(F1,text = 'رقم الفاتورة',font = ('tajawal',10),bg = '#0B2F3A',fg = 'gold')
        his_num.place(x = 242,y=100)

        
        # الحقول
        Ent_name = Entry(F1,justify = 'center')
        Ent_name.place(x = 90 , y = 42)
        Ent_phone = Entry(F1,justify = 'center')
        Ent_phone.place(x = 90,y =72)
        Ent_num = Entry(F1,justify = 'center')
        Ent_num.place(x = 90, y =102)
        # زر
        btn_Customor = Button(F1,text = 'بحث',font = ('tajawal',12),width = 10,height = 4,bg = 'gold')
        btn_Customor.place(x =3, y = 40 )
        # ============= الفاتورة ==============
        tiedd = Label(F1, text = '[الفواتير]',font = ('tajawal',13,'bold'),bg = '#0B2F3A',fg = 'gold')
        tiedd.place(x = 125,y = 135)

        F3 = Frame(root,bd = 2,width = 338,height = 399,bg = 'white')
        F3.place(x = 959,y = 205 )
        scrol_y = Scrollbar(F3,orient =VERTICAL )
        self.textarea = Text(F3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side = LEFT,fill = Y)
        scrol_y.config(command = self.textarea.yview)
        self.textarea.pack(fill = BOTH, expand = 1)
        # ======= الاسعار ======
        F4 = Frame(root,bd = 2,width = 657,height = 112,bg = '#0B2F3A' )
        F4.place(x = 641,y=595 )
        hesab = Button(F4,text = 'الحساب', width = 13,height = 1,font = 'tajawal',bg = '#DBA901')
        hesab.place(x = 537,y = 10)
        fatora = Button(F4,text = 'تصدير الفاتورة',width = 13,height =1,font = 'tajawal',bg = '#DBA901' )
        fatora.place(x = 537,y =55 )
        clear = Button(F4,text = 'افراغ الحقول',width = 13,height = 1,font = 'tajawal',bg = '#DBA901')
        clear.place(x =417,y = 10 )
        exite= Button(F4,text = 'اغلاق البرنامج',width = 13,height = 1,font = 'tajawal',bg = '#DBA901')
        exite.place(x =417,y = 55 )
        lblo1 = Label(F4,text = 'الحساب الكلي للبقوليات',font = ('tajawal',10,'bold'),bg ='#0B2F3A',fg = 'gold' )
        lblo1.place(x =220 ,y =10 )
        lblo2 = Label(F4,text = 'حساب اللوازم المنزلية',font = ('tajawal',10,'bold'),bg ='#0B2F3A',fg = 'gold' )
        lblo2.place(x =220 ,y =40 )
        lblo3 = Label(F4,text = 'حساب ادوات الكهرباء',font = ('tajawal',10,'bold'),bg ='#0B2F3A',fg = 'gold' )
        lblo3.place(x =220 ,y =70 )

        ento1= Entry(F4,textvariable = self.bocoliat,width = 24,)
        ento1.place(x = 40,y =12)

        ento2 = Entry(F4,textvariable = self.adoat,width = 24,)
        ento2.place(x = 40,y =44)

        ento3 = Entry(F4,textvariable = self.kahraba,width = 24,)
        ento3.place(x = 40,y =72)

        #=== items===
        FF1 = Frame(root,bd = 2,width = 318,height = 664,bg = '#0B2F3A')
        FF1.place(x=1,y = 33 )

        t = Label(FF1,text = 'البقوليات',font = ('tajawal',14,'bold'),bg = '#0B2F3A',fg = 'gold')
        t.place(x =122,y = 0)
        bq1 = Label(FF1,text = 'الارز',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq1.place(x = 275,y = 50) 

        EE1 = Entry(FF1,justify = 'center',textvariable = self.q1,width = 25)
        EE1.place(x = 20,y= 54)

        bq2 = Label(FF1,text = 'العدس',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq2.place(x = 270,y =100 )

        EE2 = Entry(FF1,justify = 'center',textvariable = self.q2,width = 25)
        EE2.place(x = 20,y= 104)

        bq3 = Label(FF1,text = ' الفاصولياء',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq3.place(x =240 ,y =150 )

        EE3 = Entry(FF1,justify = 'center',textvariable = self.q3,width = 25)
        EE3.place(x = 20,y= 154)

        bq4 = Label(FF1,text = 'الفول',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq4.place(x =275 ,y =200 )

        EE4 = Entry(FF1,justify = 'center',textvariable = self.q4,width = 25)
        EE4.place(x = 20,y= 204)

        bq5 = Label(FF1,text = 'الحمص',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq5.place(x =264 ,y =250 )

        EE5 = Entry(FF1,justify = 'center',textvariable = self.q5,width = 25)
        EE5.place(x = 20,y= 254)

        bq6= Label(FF1,text = 'الوبيا',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq6.place(x =276 ,y =300 )

        EE6 = Entry(FF1,justify = 'center',textvariable = self.q6,width = 25)
        EE6.place(x = 20,y= 304)

        bq7 = Label(FF1,text = 'المكارونا',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq7.place(x =255 ,y =350 )

        EE7 = Entry(FF1,justify = 'center',textvariable = self.q7,width = 25)
        EE7.place(x = 20,y= 354)

        bq8 = Label(FF1,text = 'الفلفل الاسود',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq8.place(x =230 ,y =400 )

        EE8 = Entry(FF1,justify = 'center',textvariable = self.q8,width = 25)
        EE8.place(x = 20,y= 404)

        bq9 = Label(FF1,text = 'العدس الاسمر',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq9.place(x =226 ,y =450 )

        EE9 = Entry(FF1,justify = 'center',textvariable = self.q9,width = 25)
        EE9.place(x = 20,y= 454)

        bq10 = Label(FF1,text = 'الترمس',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq10.place(x =259 ,y =500 )

        EE10 = Entry(FF1,justify = 'center',textvariable = self.q10,width = 25)
        EE10.place(x = 20,y= 504)

        bq11 = Label(FF1,text = 'الصويا',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq11.place(x =259 ,y =550 )


        EE11 = Entry(FF1,justify = 'center',textvariable = self.q11,width = 25)
        EE11.place(x = 20,y= 554)
        
        # ========= الاوازم المنزلية ========

        FF2 = Frame(root,bd = 2,width = 318,height = 664,bg = '#0B2F3A')
        FF2.place(x=320,y = 33 )

        t = Label(FF2,text = 'الوازم المنزلية',font = ('tajawal',14,'bold'),bg = '#0B2F3A',fg = 'gold')
        t.place(x =122,y = 0)

        # ======== العناوين وحقول الادخال ==========

        bq1 = Label(FF2,text = 'مسحوق ',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq1.place(x = 260,y = 50) 

        EE1 = Entry(FF2,justify = 'center',width = 25)
        EE1.place(x = 20,y= 54)

        bq2 = Label(FF2,text = 'سناكس',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq2.place(x = 260,y =100 )

        EE2 = Entry(FF2,justify = 'center',width = 25)
        EE2.place(x = 20,y= 104)

        bq3 = Label(FF2,text = 'قهوة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq3.place(x =275 ,y =150 )

        EE3 = Entry(FF2,justify = 'center',width = 25)
        EE3.place(x = 20,y= 154)

        bq4 = Label(FF2,text ='اجبان',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq4.place(x =270 ,y =200 )

        EE4 = Entry(FF2,justify = 'center',width = 25)
        EE4.place(x = 20,y= 204)

        bq5 = Label(FF2,text = 'صابون',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq5.place(x =260 ,y =250 )

        EE5 = Entry(FF2,justify = 'center',width = 25)
        EE5.place(x = 20,y= 254)

        bq6= Label(FF2,text = 'سمنة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq6.place(x =265 ,y =300 )

        EE6 = Entry(FF2,justify = 'center',width = 25)
        EE6.place(x = 20,y= 304)

        bq7 = Label(FF2,text = 'كفتة مجمدة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq7.place(x =238 ,y =350 )

        EE7 = Entry(FF2,justify = 'center',width = 25)
        EE7.place(x = 20,y= 354)

        bq8 = Label(FF2,text = 'لحوم مجمدة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq8.place(x =238 ,y =400 )

        EE8 = Entry(FF2,justify = 'center',width = 25)
        EE8.place(x = 20,y= 404)

        bq9 = Label(FF2,text = 'رايب',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq9.place(x =275 ,y =450 )

        EE9 = Entry(FF2,justify = 'center',width = 25)
        EE9.place(x = 20,y= 454)

        bq10 = Label(FF2,text = 'فراخ ',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq10.place(x =275 ,y =500 )

        EE10 = Entry(FF2,justify = 'center',width = 25)
        EE10.place(x = 20,y= 504)

        bq11 = Label(FF2,text = 'عصائر',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq11.place(x =265 ,y =550 )


        EE11 = Entry(FF2,justify = 'center',width = 25)
        EE11.place(x = 20,y= 554)
        #=============== الوازم المنزلية ==================
        FF3 = Frame(root,bd = 2,width = 318,height = 560,bg = '#0B2F3A')
        FF3.place(x=640,y = 33 )

        t3 = Label(FF3,text = 'أدوات الكهرباء',font = ('tajawal',14,'bold'),bg = '#0B2F3A',fg = 'gold')
        t3.place(x =122,y = 0)

        # ===== العناوين وحقول الادخال ======
        bq1 = Label(FF3,text = 'لمبات ',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq1.place(x = 270,y = 50) 

        EE1 = Entry(FF3,justify = 'center',width = 25)
        EE1.place(x = 20,y= 54)

        bq2 = Label(FF3,text = 'تلفاز',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq2.place(x = 270,y =100 )

        EE2 = Entry(FF3,justify = 'center',width = 25)
        EE2.place(x = 20,y= 104)

        bq3 = Label(FF3,text = 'مكوة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq3.place(x =275 ,y =150 )

        EE3 = Entry(FF3,justify = 'center',width = 25)
        EE3.place(x = 20,y= 154)

        bq4 = Label(FF3,text ='ساعة ',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq4.place(x =270 ,y =200 )

        EE4 = Entry(FF3,justify = 'center',width = 25)
        EE4.place(x = 20,y= 204)

        bq5 = Label(FF3,text = 'خلاط',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq5.place(x =265 ,y =250 )

        EE5 = Entry(FF3,justify = 'center',width = 25)
        EE5.place(x = 20,y= 254)

        bq6= Label(FF3,text = 'مكيف',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq6.place(x =265 ,y =300 )

        EE6 = Entry(FF3,justify = 'center',width = 25)
        EE6.place(x = 20,y= 304)

        bq7 = Label(FF3,text = 'مروحة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq7.place(x =260 ,y =350 )

        EE7 = Entry(FF3,justify = 'center',width = 25)
        EE7.place(x = 20,y= 354)

        bq8 = Label(FF3,text = 'ميكروويف',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq8.place(x =238 ,y =400 )

        EE8 = Entry(FF3,justify = 'center',width = 25)
        EE8.place(x = 20,y= 404)

        bq9 = Label(FF3,text = 'صاعق',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq9.place(x =265 ,y =450 )

        EE9 = Entry(FF3,justify = 'center',width = 25)
        EE9.place(x = 20,y= 454)

        bq10 = Label(FF3,text =  'مكنسة',font = ('tajawal',14),bg = '#0B2F3A',fg = 'white')
        bq10.place(x =267 ,y =500 )

        EE10 = Entry(FF3,justify = 'center',width = 25)
        EE10.place(x = 20,y= 504)




        






        
        
root = Tk()
ob = Super(root)
root.mainloop()