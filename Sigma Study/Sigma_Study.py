from tkinter import *
import pandas as pd
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from tkcalendar import Calendar
from pdf2image import convert_from_path
import webbrowser
import os
from functools import reduce


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "e.s.l.a.m",
    database = "QnA")

cursor = mydb.cursor()



def material():
    cursor.execute("select Questions from QuestionsAndAnswers")
    data = cursor.fetchall()
    
    ListForBox = [r for r, in data]
    
    #materials fun
    def week1():
        webbrowser.open_new(r'WEEK-01.pdf')
    def week2():
        webbrowser.open_new(r'WEEK-02.pdf')
    def week3():
        webbrowser.open_new(r'WEEK-03.pdf')
    def week4():
        webbrowser.open_new(r'WEEK-04.pdf')
    def week5():
        webbrowser.open_new(r'WEEK-05.pdf')
    def sec1():
        webbrowser.open_new(r'section-1.pdf')
    def sec2():
        webbrowser.open_new(r'section-2.pdf')
    def sec3():
        webbrowser.open_new(r'section-3.pdf')
    #-------------------------------------------------------------------------------------------------
    def IS1():
        webbrowser.open_new(r'Information System lec 1.pdf')
    def IS2():
        webbrowser.open_new(r'Information System lec 2.pdf')
    def IS3():
        webbrowser.open_new(r'Information System lec 4-new.pdf')
    def IS4():
        webbrowser.open_new(r'Information System lec 6.pdf')
    def IS5():
        webbrowser.open_new(r'Python .pdf')
    #---------------------------------------------------------------------------------------------------
    def oop1():
        webbrowser.open_new(r'lec-2 OOP.pdf')
    def oop2():
        webbrowser.open_new(r'lec-3-4.pdf')
    #-----------------------------------------------------------------------------------------------------
    def tw1():
        webbrowser.open_new(r'lect 2.pdf')
    def tw2():
        webbrowser.open_new(r'lect 3.pdf')
    def tw3():
        webbrowser.open_new(r'lect 4.pdf')
    def tw4():
        webbrowser.open_new(r'lect 5.pdf')
    def tw5():
        webbrowser.open_new(r'long latex.pdf')
    def tw6():
        webbrowser.open_new(r'latex -Autosaved-1.pdf')
    #---------------------------------------------------------------------------------------------------
    def math1():
        webbrowser.open_new(r'MATH.pdf')
    #---------------------------------------------------------------------------------------------------
    def ba1():
        webbrowser.open_new(r'Lecture 1.pdf')
    def ba2():
        webbrowser.open_new(r'Lecture 2.pdf')
    def ba3():
        webbrowser.open_new(r'Lecture 3.pdf')
    def ba4():
        webbrowser.open_new(r'Lecture 4.pdf')


    # button function
    def bttn(x,text,bcolor,fcolor,cmd):
        myButton1 = Button(navbar,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
        myButton1.pack(side=LEFT,padx=x)
    
    def bttn1(x,y,img,bcolor,fcolor,cmd):
        mymtrl =Button(materials,image=img,
        text='fares',
                        width=130,
                        height=130,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd
        )
        mymtrl.pack(side=LEFT,padx=x,pady=y)

    # button for pdf files
    def bttnpdf(x,y,text,bcolor,fcolor,cmd):
        myButton1 = Button(navbar,text=text,
                    width=50,
                    fg='#262626',
                    font=10,
                    border=0,
                    bg=fcolor,
                    activeforeground='#262626',
                    activebackground=bcolor,
                    cursor='hand2',         
                    command=cmd)
        myButton1.place(x=x,y=x)
    
    def lbl(x,y,txt):
        mylbl = Label(materials,
                    font=10,
                    text=txt,
        )
        mylbl.place(x=x,y=y)
    
    def IS():
        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
            myBtnpdf.place(x=x,y=y)
        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Amer Abohany',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures,6 Sections',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)

        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()
    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'week-01','#0554f2','#eee',IS1)
        bttnpdf(10,80,'week-02','#0554f2','#eee',IS2)
        bttnpdf(10,110,'week-03','#0554f2','#eee',IS3)
        bttnpdf(10,140,'week-04','#0554f2','#eee',IS4)
        bttnpdf(10,170,'Python','#0554f2','#eee',IS5)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)
        
    
    def OOP():
        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
            myBtnpdf.place(x=x,y=y)
        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Abeer Saber',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures,6 Sections',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)



        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()
    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'week-01','#0554f2','#eee',oop1)
        bttnpdf(10,80,'week-02','#0554f2','#eee',oop2)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)

    
    def PM():

        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                            width=10,
                            fg='#262626',
                            font=10,
                            border=0,
                            bg=fcolor,
                            activeforeground='#262626',
                            activebackground=bcolor,
                            cursor='hand2',         
                            command=cmd)
            myBtnpdf.place(x=x,y=y)

        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Reda M.Hussien',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures,6 Sections',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)

        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()

    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'week-01','#0554f2','#eee',week1)
        bttnpdf(10,80,'week-02','#0554f2','#eee',week2)
        bttnpdf(10,110,'week-03','#0554f2','#eee',week3)
        bttnpdf(10,140,'week-04','#0554f2','#eee',week4)
        bttnpdf(10,170,'week-05','#0554f2','#eee',week5)
        bttnpdf(10,200,'section-01','#0554f2','#eee',sec1)
        bttnpdf(10,230,'section-02','#0554f2','#eee',sec2)
        bttnpdf(10,260,'section-03','#0554f2','#eee',sec3)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)
    
    def TW():
        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
            myBtnpdf.place(x=x,y=y)
        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Mohamed Samir',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures,6 Sections',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)

        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()

    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'week-01','#0554f2','#eee',tw1)
        bttnpdf(10,80,'week-02','#0554f2','#eee',tw2)
        bttnpdf(10,110,'week-03','#0554f2','#eee',tw3)
        bttnpdf(10,140,'week-04','#0554f2','#eee',tw4)
        bttnpdf(10,170,'week-05','#0554f2','#eee',tw5)
        bttnpdf(10,200,'section-01','#0554f2','#eee',tw6)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)
    
    def MATH():
        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
            myBtnpdf.place(x=x,y=y)
        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Osama Abu Saada',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures,6 Sections',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)
        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()

    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'book','#0554f2','#eee',math1)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)
    
    def BA():
        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
            myBtnpdf.place(x=x,y=y)
        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Abeer saber',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)
        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()

    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'week-01','#0554f2','#eee',ba1)
        bttnpdf(10,80,'week-02','#0554f2','#eee',ba2)
        bttnpdf(10,110,'week-03','#0554f2','#eee',ba3)
        bttnpdf(10,140,'week-04','#0554f2','#eee',ba4)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)
    
    def DS():
        def bttnpdf(x,y,text,bcolor,fcolor,cmd):
            myBtnpdf= Button(resourses,text=text,
                        width=10,
                        fg='#262626',
                        font=10,
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        cursor='hand2',         
                        command=cmd)
            myBtnpdf.place(x=x,y=y)
        info = Frame(window,width=400,height=130,bg='#eee',border=1)
        info.place(x=10,y=270)
        l1 = Label(info, text='Lecturer :', font=('Helvetica', 14, 'bold'))
        l1.place(x=10,y=10)
        l_1 = Label(info,text='Dr.Haitham El-Wahsh',font=('Helvetica', 14))
        l_1.place(x=110,y=10)
        l2 = Label(info, text='Courses :', font=('Helvetica', 14, 'bold'))
        l2.place(x=10,y=50)
        l_2 = Label(info,text='10 lectures,6 Sections',font=('Helvetica', 14))
        l_2.place(x=110,y=50)
        l3 = Label(info, text='Duration :', font=('Helvetica', 14, 'bold'))
        l3.place(x=10,y=90)
        l_3 = Label(info,text='10 weeks',font=('Helvetica', 14))
        l_3.place(x=110,y=90)
    
        v = StringVar()
    
        bot = Frame(window,width=400,height=130,bg='#eee',border=1)
        bot.place(x=420,y=270)
    
        l4 =Label(bot,text="Q&A ", font=('Helvetica', 14, 'bold'))
        l4.place(x=10,y=7)
    
        combo = ttk.Combobox(bot,values = ListForBox, textvariable = v, width='20',height='10')
        combo.place(x=12,y=35)
    
        lbl2 = Label(bot,text='', width = 50, height = 2, wraplength=350)
        lbl2.place(x=20,y=65)
    
        def show(*args):
            cursor.execute("select Answers from QuestionsAndAnswers where Questions = " + "\"" + v.get() +"\"")
            ans = cursor.fetchall()
            #print(ans)
            lbl2.config(text = ans[0][0])
    
        
        v.trace("w",show)
        def add_QnA():
            Q = qustion.get()
            A = answer.get()
            sql = "insert into QuestionsAndAnswers(Questions,Answers) values(%s, %s)"
            data = (Q, A)
            cursor.execute(sql,data)
            mydb.commit()

    
    
        resourses= Frame(window,width=360,height=370,bg='#eee')
        resourses.place(x=830,y=270)
        bttnpdf(10,50,'week-01','#0554f2','#eee',None)
        bttnpdf(10,80,'week-02','#0554f2','#eee',None)
        l5 = Label(resourses,text='Resourses',font=('Helvetica', 14, 'bold'))
        l5.place(x=10,y=7)
        notes = Frame(window, width=810, height=230,bg='#eeeeee')
        notes.place(x=10, y=410)
        bt2 = Button(notes,text='Add Note',borderwidth=2,cursor='plus', command = lambda:[add_QnA()])
        bt2.place(x=700,y=15)
        bot_l1 = Label(notes,text='Add qustion : ',font=('Helvetica', 14, 'bold'))
        bot_l1.place(x=10,y=50)
        qustion =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        qustion.place(x=150, y=50)
        bot_l2 = Label(notes,text='Answer : ',font=('Helvetica', 14, 'bold'))
        bot_l2.place(x=10,y=100)
        answer =Entry(notes,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        answer.place(x=150, y = 100)
    
    
    
    window = Tk()
    window.title('Sigma Study')
    window.config(background='white')
    window.iconbitmap('logo_Ss.ico')
    window.geometry('1200x650+75+30')
    window.resizable(False,False)
    #navegation bar
    navbar = Frame(window, height='60', bg = '#eeeeee')
    navbar.pack(fill=X)
    photo1 = Image.open("logo_Ss-removebg-preview.png")
    resized1 =photo1.resize((50, 50),Image.ANTIALIAS)
    photo_1 = ImageTk.PhotoImage(resized1)
    label1 = Label(navbar, image=photo_1 , bg='#eee')
    label1.pack(side=LEFT,padx=80)
    #button in navbar
    bttn(20,' HOME','#0554f2','#eee',lambda:[window.destroy(), Home()])
    bttn(20,'Materials','#0554f2','#eee',lambda:[window.destroy(), material()])
    bttn(20,'profile','#0554f2','#eee',lambda:[window.destroy(), profile()])
    bttn(50,'Log out','#0554f2','#eee',lambda:[window.destroy(), sign_in()])
    mtrl = Label(window,text='Materials',bg='white',font=('Helvetica', 18, 'bold'))
    mtrl.place(x=55,y=70)
    
    #photos
    #IS
    photo2 =PhotoImage(file='info-systems.png')
    label2 = Label(image=photo2)
    #OOP
    photo3 =PhotoImage(file='maxresdefault.png')
    label3 = Label(image=photo3)
    #PM
    photo4 =PhotoImage(file='project-management-skills.png')
    label4 = Label(image=photo4)
    #TW
    photo5 =PhotoImage(file='images.png')
    label5 = Label(image=photo5)
    #MATH III
    photo6 =PhotoImage(file='math-numbers.jpg.png')
    label6 = Label(image=photo6)
    #BA
    photo7 =PhotoImage(file='bu.png')
    label7 = Label(image=photo7)
    #DS
    photo8 =PhotoImage(file='IMG_20220419_192942.png')
    label8 = Label(image=photo8)
    
    # materials
    materials = Frame(window,bg='#eee')
    materials.pack(fill=X,pady=50)
    bttn1(30,10,photo2,'#0554f2','#eee',IS)
    lbl(30,130,'Information System')
    bttn1(10,10,photo3,'#0554f2','#eee',OOP)
    lbl(205,130,'Object oriented        ')
    bttn1(10,10,photo4,'#0554f2','#eee',PM)
    lbl(360,130,'Project Management')
    bttn1(10,10,photo5,'#0554f2','#eee',TW)
    lbl(515,130,' Technical Writing   ')
    bttn1(10,10,photo6,'#0554f2','#eee',MATH)
    lbl(670,130,'Math III                      ')
    bttn1(10,10,photo7,'#0554f2','#eee',BA)
    lbl(820,130,'B.Administration       ')
    bttn1(10,10,photo8,'#0554f2','#eee',DS)
    lbl(980,130,'  Discrete Structures       ')
    
    
    
    
    
    window.mainloop()



def profile():
    

    window = Tk()
    window.geometry("1200x650+75+30")
    window.config(bg="white")
    window.resizable(False,False)


    def bttn(x,text,bcolor,fcolor,cmd):
        myButton1 = Button(navbar,text=text,
                    width=10,
                    fg='#262626',
                    font=10,
                    border=0,
                    bg=fcolor,
                    activeforeground='#262626',
                    activebackground=bcolor,
                    cursor='hand2',         
                    command=cmd)
        myButton1.pack(side=LEFT,padx=x)

    id_0 = results[0][0]
    def edit():
        lvl = lev.get()
        sect = sec.get()
        division = dev.get()

        sql1 = "UPDATE PFS SET LvL = " + "\"" + lvl + "\"" + " WHERE id = " + str(results[0][0]) 
        sql2 = "UPDATE PFS SET section = " + "\"" + sect + "\"" + " WHERE id = " + str(results[0][0]) 
        sql3 = "UPDATE PFS SET Division = " + "\"" + division + "\"" + " WHERE id = " + str(results[0][0]) 

        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)

        mydb.commit()
     
    def update():
        results = None
        sql = "select * from PFS where id = " + str(id_0)
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            for i in results:
                break   
        l.config(text = results[0][2])
        d.config(text = results[0][3])
        S.config(text = results[0][6])

    def delete():
        sql = "delete from PFS where id = " + str(results[0][0])
        cursor.execute(sql)
        mydb.commit()


    #navegation bar
    navbar = Frame(window, height='60', bg = '#eeeeee')
    navbar.pack(fill=X)
    photo1 = Image.open("logo_Ss-removebg-preview.png")
    resized1 =photo1.resize((50, 50),Image.ANTIALIAS)
    photo_1 = ImageTk.PhotoImage(resized1)
    label1 = Label(navbar, image=photo_1 , bg='#eee')
    label1.pack(side=LEFT,padx=80)
    #button in navbar
    bttn(20,' HOME','#0554f2','#eee',lambda:[window.destroy(), Home()])
    bttn(20,'Materials','#0554f2','#eee',lambda:[window.destroy(), material()])
    bttn(20,'profile','#0554f2','#eee',lambda:[window.destroy(), profile()])
    bttn(50,'Log out','#0554f2','#eee',lambda:[window.destroy(), sign_in()])
    mtrl = Label(window,text='Materials',bg='white',font=('Helvetica', 18, 'bold'))
    mtrl.place(x=55,y=70)



    # student info
    side = Frame(window, bg="#14aaf5", width=700, height=940)
    side.place(x=0, y=55)
    name = Label(side, text="Name: ", font="Helvetica 15 bold",bg="#14aaf5",fg="white")
    name.place(x=10, y=100)
    N = Label(text=results[0][1],font="Helvetica 15 ",bg="#14aaf5",fg="white")
    N.place(x=80, y=155)
    
    id = Label(side, text="Id: ", font="Helvetica 15 bold",bg="#14aaf5",fg="white")
    id.place(x=10, y=170)
    i = Label(text=results[0][0], font="Helvetica 15 ",bg="#14aaf5",fg="white")
    i.place(x=40, y=225)
    
    level = Label(side, text="Level: ", font="Helvetica 15 bold",bg="#14aaf5",fg="white")
    level.place(x=10, y=240)
    l = Label(text=results[0][2], font="Helvetica 15 ",bg="#14aaf5",fg="white")
    l.place(x=75, y=295)
    
    email = Label(side, text="Email: ", font="Helvetica 15 bold",bg="#14aaf5",fg="white")
    email.place(x=10, y=310)
    E = Label(text=results[0][4], font="Helvetica 15 ",bg="#14aaf5",fg="white")
    E.place(x=80, y=365)
    
    devision = Label(side, text="Devision: ", font="Helvetica 15 bold",bg="#14aaf5",fg="white")
    devision.place(x=10, y=380)
    d = Label(text=results[0][3], font="Helvetica 15 ",bg="#14aaf5",fg="white")
    d.place(x=105, y=435)
    
    section = Label(side, text="Section: ", font="Helvetica 15 bold",bg="#14aaf5",fg="white")
    section.place(x=10, y=450)
    S = Label(text=results[0][6], font="Helvetica 15 ",bg="#14aaf5",fg="white")
    S.place(x=95, y=505)
    
    # student's bio
    eb=Button(window,text="Edit",font="Helvetica 10 ",fg="#14aaf5",bg="white", command = lambda:[edit(), update(), window.destroy() ,sign_in()])
    eb.place(x=720,y=400)
    levl=Label(window,text="level",font="Helvetica 10  ",fg="#14aaf5",bg="white")
    levl.place(x=720,y=440)
    lev=Entry(window)
    lev.place(x=780,y=440)

    devl=Label(window,text="Devision",font="Helvetica 10  ",fg="#14aaf5",bg="white")
    devl.place(x=720,y=460)
    dev=Entry(window)
    dev.place(x=780,y=460)

    secl=Label(window,text="Section",font="Helvetica 10 ",fg="#14aaf5",bg="white")
    secl.place(x=720,y=480)
    sec=Entry(window)
    sec.place(x=780,y=480)
  
    delet=Button(window,text="delete",font="Helvetica 10  ",fg="#14aaf5",bg="white", command = lambda: [delete(), window.destroy(), sign_in()])
    delet.place(x=930,y=600)

    
    
    
    
    
    window.mainloop()


def Home():
    tk = Tk()
    tk.geometry("1200x650+75+30")
    tk.resizable(False,False)
    
    
    def bttn(x,text,bcolor,fcolor,cmd):
        myButton1 = Button(navbar,text=text,
                    width=10,
                    fg='#262626',
                    font=10,
                    border=0,
                    bg=fcolor,
                    activeforeground='#262626',
                    activebackground=bcolor,
                    cursor='hand2',         
                    command=cmd)
        myButton1.pack(side=LEFT,padx=x)
    
    #navegation bar
    navbar = Frame(tk, height='60', bg = '#eee')
    navbar.pack(fill=X)
    photo1 = Image.open("logo_Ss-removebg-preview.png")
    resized1 =photo1.resize((50, 50),Image.ANTIALIAS)
    photo_1 = ImageTk.PhotoImage(resized1)
    label1 = Label(navbar, image=photo_1 , bg='#eee')
    label1.pack(side=LEFT,padx=80)
    #button in navbar
    bttn(20,' HOME','#0554f2','#eee',lambda:[tk.destroy(), Home()])
    bttn(20,'Materials','#0554f2','#eee',lambda:[tk.destroy(), material()])
    bttn(20,'profile','#0554f2','#eee',lambda:[tk.destroy(), profile()])
    bttn(50,'Log out','#0554f2','#eee',lambda:[tk.destroy(), sign_in()])
    
    
    
    
    
    cal = Calendar(tk, selectmode = "day")
    v = StringVar(tk ,value= cal.get_date())
     
    cal = Calendar(textvariable = v, date_pattern = "yyyy-mm-dd")
    cal.pack(fill = "x", ipady = 30)
    
    for i in range(6):
        cal._week_nbs[i].destroy()
     

    
    
    def get_note(*args): 
        cursor.execute("select note from NIT where curdate = " + "\"" + v.get() +"\"")
        note = cursor.fetchall()
        date = pd.Timestamp(v.get())
        print(v.get(),date.day_name())
    
        cursor.execute("select L from Lecture where today = " + "\"" + date.day_name() +"\"")
        lect = cursor.fetchall()

        cursor.execute("select " + date.day_name() + " from Sections where sect = " + str(results[0][6]))
        sect = cursor.fetchall()

 
        
        print(lect[0][0], results[0][6])
    
        if not note:


            nin.config(text = sect[0][0])
            ele.config(text = sect[1][0])
            one.config(text = sect[2][0])

            tx.config(text = "nothing to do")
        else:
            nin.config(text = sect[0][0])
            ele.config(text = sect[1][0])
            one.config(text = sect[2][0])


                
            tx.config(text = reduce(lambda x, y: (x[0] + "\n" + y[0],), note)[0])



    v.trace("w", get_note)
    
    tx=Label(tk,width=50,height=10, text = "", bg = "#14aaf5")
    tx.place(x=20,y=490)
    
    def add_note():
        note = ent.get()
        sql = ("insert into NIT(curdate, note) values(%s, %s)")
        cursor.execute(sql,[(v.get()), (note)])
        mydb.commit()
    
    la=Label(text="Add note", font="Helvetica 10 ",fg="#14aaf5")
    la.place(x=50,y=300)
    ent=Entry(tk)
    ent.place(x=110,y=300)
    btn=Button(tk,text="upload",fg="#14aaf5",bg="white", command = lambda: [add_note()])
    btn.place(x=70,y=350)
    
    #the main body
    sch=LabelFrame(tk,text="sections' schediles",width=600,height=300,font="Helvetica 15 bold",pady=10,border=5)
    sch.place(x=840,y=510)
    #titles inside the labelfram
    Label(sch,text="9:00/11:00",padx=12.5,font="Helvetica 13 bold" ).grid(column=0,row=0)
    #the content under the time 
    nin = Label(sch,text="",padx=5, pady = 20,font="Helvetica 10 bold")
    nin.grid(column=0,row=2)
    #VERTICAL separator
    ttk.Separator(master=sch,orient=VERTICAL,class_=ttk.Separator,takefocus=1).grid(column=1,row=0,sticky=NS)
    
    Label(sch,text="11:00/1:00",padx=25,font="Helvetica 13 bold").grid(column=2,row=0)
    #the content under the time
    ele = Label(sch,text="",padx=12.5, pady = 20,font="Helvetica 10 bold")
    ele.grid(column=2,row=2)
    
    #VERTICAL separator
    ttk.Separator(master=sch,orient=VERTICAL,class_=ttk.Separator,takefocus=1).grid(column=3,row=0,sticky=NS)
    Label(sch,text="1:00/3:00",padx=12.5,font="Helvetica 13 bold").grid(column=4,row=0)
    #the content under the time 
    one = Label(sch,text="", pady = 20,font="Helvetica 10 bold")
    one.grid(column=4,row=2)
    
    
    tk.mainloop()


def Register():

    
    win = Tk()
    win.geometry('925x500+300+200')
    win.title('Sign-Up')
    
    win.configure(bg='#fff')
    win.resizable(False,False)
    
    win.iconbitmap('logo_Ss.ico')
    
    
    
    img =PhotoImage(file="login.png")
    Label(win,image=img,border=0,bg='white').place(x=380,y=40)
    
    
    frame=Frame(win)
    frame.place(x=50, y=100)
    
    heading=Label(frame,text='Sign-Up' ,fg='#57a1f8' ,bg='white' ,font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    
    v1 = StringVar()
    l1 = Label(win, bg='#fff',textvariable = v1, width = 15).grid(row = 2, column = 2)
    v1.set("UserName")
    name = Entry(win, width = 30)
    name.grid(row = 2, column = 3)
    
    
    v2 = StringVar()
    l2 = Label(win, bg='#fff',textvariable = v2, width = 15).grid(row = 3, column = 2)
    v2.set("ID")
    id = Entry(win, width = 30)
    id.grid(row = 3, column = 3)
    
    v3 = StringVar()
    l3 = Label(win,bg='#fff', textvariable = v3, width = 15).grid(row = 4, column = 2)
    v3.set("Email")
    email = Entry(win, width = 30)
    email.grid(row = 4, column = 3)
    
    v4 = StringVar()
    l4 = Label(win,bg='#fff', textvariable = v4, width = 15).grid(row = 5, column = 2)
    v4.set("Password")
    pw = Entry(win, width = 30)
    pw.grid(row = 5, column = 3)
    
    v5 = StringVar()
    l5 = Label(win,bg='#fff', textvariable = v5, width = 15).grid(row = 6, column = 2)
    v5.set("Section")
    sec = Entry(win, width = 30)
    sec.grid(row = 6, column = 3)
    
    v6 = StringVar()
    l6 = Label(win,bg='#fff', textvariable = v6, width = 15).grid(row = 7, column = 2)
    v6.set("Level")
    lvls = ["First", "Second", "Third", "Fourth"]
    lvl = ttk.Combobox(win, values = lvls, width = 20)
    lvl.grid(row = 7, column = 3)
    
    v7 = StringVar()
    l7 = Label(win,bg='#fff', textvariable = v7, width = 15).grid(row = 8, column = 2)
    v7.set("Division")
    divs = ["CS", "IT", "SE", "IS", "BIO", "General"]
    div = ttk.Combobox(win, values = divs, width = 20)
    div.grid(row = 8, column = 3)
    
    b = Button(win, text = "Register", command = lambda:[add_data(), win.destroy(), sign_in()])
    b.grid(row = 9, column = 3)

    b = Button(win, text = "Login", command = lambda:[win.destroy(), sign_in()])
    b.grid(row = 10, column = 3)

    l8 = Label(win,  text = "")
    l8.grid(row = 11, column = 3) 

    def add_data():
        valid = True
        Name = name.get()
        ID = id.get()
        Email = email.get()
        PW = pw.get()
        Sec = sec.get()
        Lvl = lvl.get()
        Div = div.get()
    
        cursor.execute("select * from PFS where id = " + "\"" + ID +"\"")
        rs = cursor.fetchall()
        no = len(rs)
        if (no > 0):
            valid = False
            l8.config(text = "id exists select different one")
    
        cursor.execute("select * from PFS where id = " + "\"" + Email +"\"")
        rs1 = cursor.fetchall()
        no1 = len(rs1)
        if (no1 > 0):
            valid = False
            l8.config(text = "Email exists select different one")
    
        if(valid):    
            data = (ID, Name, Lvl, Div, Email, PW, Sec)
            my_query = "insert into PFS(id, StudentName, LvL, Division, email, PW, section) values(%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(my_query, data)
    
            mydb.commit()
            messagebox.showinfo("Register", "Done")


    win.mainloop()


def sign_in():
    root =Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)
    
    root.iconbitmap('logo_Ss.ico')
    
    
    
    def signin():
        global results
        ID = user.get()
        Password=code.get()
        valid = True
        
        sql = "select * from PFS where id = %s and PW = %s"
        cursor.execute(sql,[(ID),(Password)])
        results = cursor.fetchall()
        if results:
            for i in results:
                print("done ", i)
                break
        else:
            messagebox.showerror("Invalid", "Invalid ID or password") 
            root.destroy()
            sign_in()
    
    img =PhotoImage(file='sssss.png')
    Label(root,image=img,bg='white').place(x=50, y=50)
    
    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)
    
    heading=Label(frame,text='Log-in' ,fg='#57a1f8' ,bg='white' ,font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    
    
    #########-------------------------
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0, 'Password')
    
    
    
    user =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30, y=80)
    user.insert(0, 'ID')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    
    
    ##################---------------------
    code =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    
    #############---------------
    Button(frame,width=39,pady=7,text='Sign-in',bg='#57a1f8' ,fg='white',border=0,command=lambda:[signin(), root.destroy(), Home()]).place(x=35,y=204)
    label=Label(frame,text="Do not have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75 ,y=270)
    
    
    
    sign_up=Button(frame, width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8', command = lambda:[root.destroy(), Register()])
    sign_up.place(x=75 ,y=270)
    
    
    root.mainloop()















#-----------------------------------------------------------------------------------------------------------------------------------
root =Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

root.iconbitmap('logo_Ss.ico')



def signin():
    global results
    ID = user.get()
    Password=code.get()
    valid = True

    print(ID, Password)
    sql = "select * from PFS where id = %s and PW = %s"
    cursor.execute(sql,[(ID),(Password)])
    results = cursor.fetchall()
    if results:
        for i in results:
            print("done ", i)
            break
    else:
        print("a7a")
        messagebox.showerror("Invalid", "Invalid ID or password")
        root.destroy()
        sign_in()
        


img =PhotoImage(file='sssss.png')
Label(root,image=img,bg='white').place(x=50, y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Log-in' ,fg='#57a1f8' ,bg='white' ,font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


#########-------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')



user =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=80)
user.insert(0, 'ID')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##################---------------------
code =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#############---------------
Button(frame,width=39,pady=7,text='Sign-in',bg='#57a1f8' ,fg='white',border=0, command = lambda:[signin(), root.destroy(), Home()]).place(x=35,y=204)
label=Label(frame,text="Do not have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75 ,y=270)



sign_up=Button(frame, width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8', command = lambda:[root.destroy(), Register()])
sign_up.place(x=75 ,y=270)


root.mainloop()




