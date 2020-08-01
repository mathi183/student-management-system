''''

    Python Code for student maintenance & management with DB connectivity
    version="1.0",
    description="Student management system by https://mathiconsultant.com",
    author = "Manikanda Dhasarathi.S.P",
    name = "Student Management System",

'''

#############################################################################################

def updatestudent():
    def update():
        pass
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        try:
            strr = 'update student_data set Name=%s,Mobile=%s,Email=%s,Address=%s, Gender=%s, DOB=%s,Date=%s,Time=%s where Id=%s'
            mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
            con.commit()
            messagebox.showinfo('Notifications', 'Id{} modified successfully......'.format(id),parent=updateroot)
            strr = 'select * from student_data'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        except:
            messagebox.showerror('Notifications','Check Database Connection or Incorrect data for updation',parent=updateroot)
            return

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x540+220+200')
    updateroot.title('Student Management System')
    updateroot.config(bg='gold')
    updateroot.iconbitmap('mathi.ico')
    updateroot.resizable(False,False)
    #----------------------------------- update Student Label
    idlabel = Label(updateroot,text= 'Enter Id : ', bg = 'gold',font=('times',20,'bold'),relief=RIDGE,
                    borderwidth = 3,width = 12,anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=50)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=90)

    emaillabel = Label(updateroot, text='Enter Email : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=130)

    addresslabel = Label(updateroot, text='Enter Address : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=170)

    genderlabel = Label(updateroot, text='Enter Gender : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=210)

    doblabel = Label(updateroot, text='Enter D.O.B : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=250)

    datelabel = Label(updateroot, text='Enter Date : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                     borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=290)

    timelabel = Label(updateroot, text='Enter Time : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=330)

    #--------------------------------------update Entry

    idval = StringVar()
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=6,textvariable=idval)
    identry.place(x=230,y=10)

    nameval = StringVar()
    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=6,textvariable=nameval)
    nameentry.place(x=230,y=50)

    mobval = StringVar()
    mobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=mobval)
    mobentry.place(x=230, y=90)

    emailval = StringVar()
    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=emailval)
    emailentry.place(x=230, y=130)

    addressval = StringVar()
    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=addressval)
    addressentry.place(x=230, y=170)

    genderval = StringVar()
    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=genderval)
    genderentry.place(x=230, y=210)

    dobval = StringVar()
    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=dobval)
    dobentry.place(x=230, y=250)

    dateval = StringVar()
    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=dateval)
    dateentry.place(x=230, y=290)

    timeval = StringVar()
    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=6, textvariable=timeval)
    timeentry.place(x=230, y=330)

    #------------------- submit button

    submitbtn = Button(updateroot, text='submit', font=('roman',15,'bold'),width=20,bd=5,
                       activebackground = 'green3', activeforeground = 'white',command=update)
    submitbtn.place(x=150,y=380)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()

######################################################################################################

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        added_date = time.strftime("%d/%m/%Y")
        try:
            if(id != ''):
                strr = 'select * from student_data where Id=%s'
                mycursor.execute(strr,(id))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif(name != ''):
                strr = 'select * from student_data where Name=%s'
                mycursor.execute(strr,(name))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif(mobile != ''):
                strr = 'select * from student_data where Mobile=%s'
                mycursor.execute(strr,(mobile))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif (email != ''):
                strr = 'select * from student_data where Email=%s'
                mycursor.execute(strr, (email))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif(address != ''):
                strr = 'select * from student_data where Address=%s'
                mycursor.execute(strr,(address))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif(gender != ''):
                strr = 'select * from student_data where Gender=%s'
                mycursor.execute(strr,(gender))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif(dob != ''):
                strr = 'select * from student_data where DOB=%s'
                mycursor.execute(strr,(dob))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)

            elif(added_date != ''):
                strr = 'select * from student_data where Date=%s'
                mycursor.execute(strr,(added_date))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studenttable.insert('', END, values=vv)
        except:
            messagebox.showerror('Notifications','Check Database connection or Incorrect data entered')
            return


    searchroot =  Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='gold')
    searchroot.iconbitmap('mathi.ico')
    searchroot.resizable(False,False)
    #----------------------------------- search Student Label
    idlabel = Label(searchroot,text= 'Enter Id : ', bg = 'gold',font=('times',20,'bold'),relief=RIDGE,
                    borderwidth = 3,width = 12,anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=50)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=90)

    emaillabel = Label(searchroot, text='Enter Email : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=130)

    addresslabel = Label(searchroot, text='Enter Address : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=170)

    genderlabel = Label(searchroot, text='Enter Gender : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=210)

    doblabel = Label(searchroot, text='Enter D.O.B : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=250)

    datelabel = Label(searchroot, text='Enter Date : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                     borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=290)

    #--------------------------------------Search Entry

    idval = StringVar()
    identry = Entry(searchroot,font=('roman',15,'bold'),bd=6,textvariable=idval)
    identry.place(x=230,y=10)

    nameval = StringVar()
    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=6,textvariable=nameval)
    nameentry.place(x=230,y=50)

    mobval = StringVar()
    mobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=6, textvariable=mobval)
    mobentry.place(x=230, y=90)

    emailval = StringVar()
    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=6, textvariable=emailval)
    emailentry.place(x=230, y=130)

    addressval = StringVar()
    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=6, textvariable=addressval)
    addressentry.place(x=230, y=170)

    genderval = StringVar()
    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=6, textvariable=genderval)
    genderentry.place(x=230, y=210)

    dobval = StringVar()
    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=6, textvariable=dobval)
    dobentry.place(x=230, y=250)

    dateval = StringVar()
    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=6, textvariable=dateval)
    dateentry.place(x=230, y=290)

    #------------------- submit button

    submitbtn = Button(searchroot, text='submit', font=('roman',15,'bold'),width=20,bd=5,
                       activebackground = 'green3', activeforeground = 'white',command=search)
    submitbtn.place(x=150,y=340)

    searchroot.mainloop()
#########################################################################################

def addstudent():
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='gold')
    addroot.iconbitmap('mathi.ico')
    addroot.resizable(False,False)
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        added_date = time.strftime("%d/%m/%Y")
        added_time = time.strftime("%H:%M:%S")
        try:
            strr = 'insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,added_date,added_time))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added Successfully...Form needs to be emptied'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
            strr = 'select * from student_data'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        except:
            messagebox.showerror('Notification', 'Check for Database Connection or Check of ID Field (it should not be empty or duplicated), Try Another...',parent=addroot)
            strr = 'select * from student_data'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)



    #----------------------------------- Add Student Label
    idlabel = Label(addroot,text= 'Enter Id : ', bg = 'gold',font=('times',20,'bold'),relief=RIDGE,
                    borderwidth = 3,width = 12,anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=50)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=90)

    emaillabel = Label(addroot, text='Enter Email : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=130)

    addresslabel = Label(addroot, text='Enter Address : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=170)

    genderlabel = Label(addroot, text='Enter Gender : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=210)

    doblabel = Label(addroot, text='Enter D.O.B : ', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                    borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=250)

    #--------------------------------------Student Entry

    idval = StringVar()
    identry = Entry(addroot,font=('roman',15,'bold'),bd=6,textvariable=idval)
    identry.place(x=230,y=10)

    nameval = StringVar()
    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=6,textvariable=nameval)
    nameentry.place(x=230,y=50)

    mobval = StringVar()
    mobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=6, textvariable=mobval)
    mobentry.place(x=230, y=90)

    emailval = StringVar()
    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=6, textvariable=emailval)
    emailentry.place(x=230, y=130)

    addressval = StringVar()
    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=6, textvariable=addressval)
    addressentry.place(x=230, y=170)

    genderval = StringVar()
    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=6, textvariable=genderval)
    genderentry.place(x=230, y=210)

    dobval = StringVar()
    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=6, textvariable=dobval)
    dobentry.place(x=230, y=250)

    #------------------- submit button

    submitbtn = Button(addroot, text='submit', font=('roman',15,'bold'),width=20,bd=5,
                       activebackground = 'green3', activeforeground = 'white',command=submitadd)
    submitbtn.place(x=150,y=320)

    addroot.mainloop()

    ###################################################################################


    #######################################################################################

def deletestudent():
    try:
        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values'][0]
        strr = 'delete from student_data where Id=%s'
        mycursor.execute(strr,(pp))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} deleted successfully'.format(pp))

        strr = 'select * from student_data'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)
    except:
        messagebox.showerror('Notifications','Check Database Connection or if Database is connected, select a record for deletion by clicking Show All')
        return


def show():
    try:
        strr = 'select * from student_data'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)
    except:
        messagebox.showerror('Notifications','Connect To Database')
        return

def export():
    try:
        strr = 'select * from student_data'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

        ff = filedialog.asksaveasfilename()
        gg = studenttable.get_children()
        id,name,mobile,email,address,gender,dob,added_date,added_time=[],[],[],[],[],[],[],[],[]
        for i in gg:
            content = studenttable.item(i)
            pp = content["values"]
            id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),added_date.append(pp[7]),added_time.append(pp[8])

        dd = ['Id','Name','Mobile','Email','Address','Gender','DOB','Date','Time']
        df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,added_date,added_time)),columns=dd)

        paths = r'{}.csv'.format(ff)
        rf = df.to_csv(paths.format(ff,),index=False)
        #if ff.endswith('.csv'):
        messagebox.showinfo('Notifications','Student Data is Saved {}'.format(paths))

    except:
        messagebox.showerror('Notifications','Connect To Database')
        return


def exit():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if(res == True):
        root.destroy()

###################################################################### Connection of Database

def Connectdb():
    def submitDB():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passval.get()

        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','login credentials are incorrect....Please Check',parent=dbroot)
            return


        try:
            strr = 'create database student_management_system1'
            mycursor.execute(strr)
            strr = 'use student_management_system1'
            mycursor.execute(strr)
            strr = 'create table student_data(Id int, Name varchar(20), Mobile varchar(12), Email varchar(25),Address varchar(50), Gender varchar(10), DOB varchar(50), Date varchar(50), Time varchar(50));'
            mycursor.execute(strr)
            strr = 'alter table student_data modify column Id int not null'
            mycursor.execute(strr)
            strr = 'alter table student_data modify column Id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and now you are connected......', parent=dbroot)



        except:
            strr = 'use student_management_system1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database......', parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('450x250+800+230')
    dbroot.iconbitmap('mathi.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='gold', relief=RIDGE)
    #-------------------------Connect DB Labels

    hostlabel = Label(dbroot, text="Enter Host :", bg = 'gold', font =('chiller',15,'bold'),
                    relief=RIDGE,borderwidth=5,width=15,anchor='w')
    hostlabel.place(x=10,y=10)

    namelabel = Label(dbroot, text="Enter Username :", bg='gold', font=('chiller', 15, 'bold'),
                    relief=RIDGE, borderwidth=5, width=15, anchor='w')
    namelabel.place(x=10, y=70)

    passlabel = Label(dbroot, text="Enter Password :", bg='gold', font=('chiller', 15, 'bold'),
                    relief=RIDGE, borderwidth=5, width=15, anchor='w')
    passlabel.place(x=10, y=130)

    #-------------------------------------- ConnectionDB Entries
    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()


    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5, width=21, textvariable=hostval)
    hostentry.place(x=210,y=10)

    nameentry = Entry(dbroot,font=('roman',15,'bold'),bd=5, width=21, textvariable=userval)
    nameentry.place(x=210,y=70)

    passentry = Entry(dbroot,font=('roman',15,'bold'),bd=5, width=21, textvariable=passval, show='*')
    passentry.place(x=210,y=130)

    #---------------------------------------Connectdb button

    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),width=10,
                          activebackground = 'green3', activeforeground = 'white',command=submitDB)
    submitbutton.place(x=170,y=190)

    dbroot.mainloop()

########################################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)

#################################################################Intro Slider

import random
colors = ['white' , 'red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']
def IntroLabelColorTrick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20,IntroLabelColorTrick)

def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count = 37
        text = 'Mathi\'S Class room - Student Portal'
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTrick)

#################################################### Student Entry Slider

colors1 = ['white' , 'red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']

def IntroLabelColorTrick1():
    fg = random.choice(colors1)
    frontlabel.config(fg=fg)
    frontlabel.after(20,IntroLabelColorTrick1)

def IntroLabelTrick1():
    global count1,text1
    if(count1>=len(aa)):
        count1 = 15
        text1 = 'Data Operations'
        frontlabel.config(text=text1)
    else:
        text1 = text1+aa[count1]
        frontlabel.config(text=text1)
        count1 += 1
    frontlabel.after(200,IntroLabelTrick1)



############################################################################# bottom_slider


colors2 = ['white']

def IntroLabelColorTrick2():
    fg = random.choice(colors2)
    SliderBottom.config(fg=fg)
    SliderBottom.after(20,IntroLabelColorTrick2)

def IntroLabelTrick2():
    global count2,text2
    if(count2>=len(bb)):
        count2 = 0
        text2 = ''
        SliderBottom.config(text=text2)
    else:
        text2 = text2+bb[count2]
        SliderBottom.config(text=text2)
        count2 += 1
    SliderBottom.after(200,IntroLabelTrick2)




#####################################################################

from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
from pandas import *
import pandas
import pymysql
import random
import time
root = Tk()
root.title('student management system')
root.config(bg='green')
root.geometry('1200x700+50+50')
root.iconbitmap('mathi.ico')
root.resizable(False,False)

########################################################################## Bottom Labael

BottomFrame = Frame(root, bg='gold', relief=RIDGE, borderwidth=5)
BottomFrame.place(x=10,y=630,width=1175,height=50)

bb = "Software Designed by Manikanda D Prabakaran (Website: https://mathiconsultant.com , Contact: 9742904692) "
count2 = 0
text2 = ''
#####################################################################

SliderBottom = Label(BottomFrame,text=bb, font=('roman',15,'bold'),relief=RIDGE, borderwidth=5, width=140, bg = 'grey',foreground='white')
SliderBottom.pack(side=TOP,expand=True)
IntroLabelTrick2()
IntroLabelColorTrick2()


###############################################################Frames

DataEntryFrame = Frame(root, bg='gold', relief=RIDGE, borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=200,height=550)

###################################################################### dataentry_Frame_Intro

aa = 'Data Operations'
count1 = 0
text1 = ''


frontlabel = Label(DataEntryFrame,text = aa,width=30,font=('roman',15,'bold'),bg='green')
frontlabel.pack(side=TOP,expand=True)
IntroLabelTrick1()
IntroLabelColorTrick1()


addbtn= Button(DataEntryFrame,text='Add Student',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=addstudent,foreground = 'white')
addbtn.pack(side=TOP,expand=True)

searchbtn= Button(DataEntryFrame,text='Search Student',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=searchstudent,foreground = 'white')
searchbtn.pack(side=TOP,expand=True)

deletebtn= Button(DataEntryFrame,text='Delete Student',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=deletestudent,foreground = 'white')
deletebtn.pack(side=TOP,expand=True)

updatebtn= Button(DataEntryFrame,text='Update Student',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=updatestudent,foreground = 'white')
updatebtn.pack(side=TOP,expand=True)

showbtn= Button(DataEntryFrame,text='Show All',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=show,foreground = 'white')
showbtn.pack(side=TOP,expand=True)

exportbtn= Button(DataEntryFrame,text='Export Data',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=export,foreground = 'white')
exportbtn.pack(side=TOP,expand=True)

exitbtn= Button(DataEntryFrame,text='Exit',width=14,font=('roman',15,'bold'),
               bd=6,bg='grey',activebackground = 'green3',activeforeground = 'white',command=exit,foreground = 'white')
exitbtn.pack(side=TOP,expand=True)



######################################################################## Show Data Frame

ShowDataFrame = Frame(root, bg='gold', relief=RIDGE, borderwidth=5)
ShowDataFrame.place(x=200,y=80,width=980,height=550)

#--------------------------------------------------------- show frame config

style = ttk.Style()
style.configure('Treeview.Heading',font=('roman',20,'bold'),foreground='black',bg='black')
style.configure('Treeview',font=('roman',15,'bold'),foreground='black',bg='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Id', 'Name', 'Mobile No', 'Email', 'Address' , 'Gender',
                                               'D.O.B', 'Added Date', 'Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text = 'Id')
studenttable.heading('Name',text = 'Name')
studenttable.heading('Mobile No',text = 'Mobile No')
studenttable.heading('Email',text = 'Email')
studenttable.heading('Address',text = 'Address')
studenttable.heading('Gender',text = 'Gender')
studenttable.heading('D.O.B',text = 'D.O.B')
studenttable.heading('Added Date',text = 'Added Date')
studenttable.heading('Added Time',text = 'Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)

##################################################################Slider
ss = "Mathi'S Class room - Students Portal"
count = 0
text = ''
#####################################################################

SliderLabel = Label(root,text=ss, font=('calibiri',20,'bold'),relief=RIDGE, borderwidth=5, width=40, bg = 'grey')
SliderLabel.place(x=260,y=7)
IntroLabelTrick()
IntroLabelColorTrick()

#################################################################### Clock

clock = Label(root,font=('roman',15,'bold'), relief=RIDGE,borderwidth=5, width=17, bg='gold')
clock.place(x=10,y=7)
tick()

##################################################################### Connect to DB button

connectbutton = Button(root,text='connect to database', width=22, font=('roman',15,'bold'),
                        borderwidth=5, bd=6, activebackground='green3',
                       activeforeground='white', command=Connectdb)
connectbutton.place(x=960,y=7)

root.mainloop()






