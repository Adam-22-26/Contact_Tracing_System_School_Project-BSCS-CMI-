from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import time as delay
from mysqlconnector_tkinter import  Database
from Person import Person
from Establishment import Establishment

class Home(Tk):
    
    def __init__(self):
        Tk.__init__(self)

        self.geometry('700x520+0+0')
        self.title('Home')
        #self.configure(bg='green')
        self.resizable(False,False)
        self.registrationForm()
        self._covidInfo()
    
                
    def _covidInfo(self):

        imgp = Image.open('./c1.png')
        self.imgresized = imgp.resize((670,250), Image.ANTIALIAS)
        self.image00 = ImageTk.PhotoImage(self.imgresized)
        self.label = ttk.Label(self.regFrame, image=self.image00)
        self.label.place(x=5, y=20)
            
        imgpath01 = Image.open('./person.png')
        self.resize01 = imgpath01.resize((100,100), Image.ANTIALIAS)
        self.imagerender01 = ImageTk.PhotoImage(self.resize01)
        self.image01 = Label(self.regFrame,image=self.imagerender01)
        self.image01.place(x=130,y=340)

        
        imgpath02 = Image.open('./est.jpg')
        self.resize02 = imgpath02.resize((100,100), Image.ANTIALIAS)
        self.imagerender02 = ImageTk.PhotoImage(self.resize02)
        self.image02 = Label(self.regFrame,image=self.imagerender02)
        self.image02.place(x=450,y=340)
        
    def registrationForm(self):
        
        self.regFrame = ttk.Frame(self, borderwidth = 2, height=710, width=590)
        self.regFrame.place(x = 5 , y=5)
        labelframe = ttk.LabelFrame(self.regFrame, text="Choose where you going to Register",width=685, height=505)
        labelframe.pack(fill="both", expand="yes")

        self.btnStyle = ttk.Style()
        self.btnStyle.configure('TButton', font=('times new roman', 12, 'bold'))
        
                
        self.PerReg =  ttk.Button(self.regFrame,style = 'TButton', text='PERSON',command=self.OpenPersonReg)
        self.PerReg.place(x=10, y =280, height = 30, width=330)
        
        self.estReg =  ttk.Button(self.regFrame, style ='TButton', text='ESTABLISHMENT', command=self.OpenEstForm)
        self.estReg.place(x=345, y =280, height = 30, width=330)
        
        self.exitWindow = ttk.Button(self.regFrame, style ='TButton', text='EXIT',  command=self.exit)
        self.exitWindow.place(x=10, y =465, height = 30, width=665)
        
        self._covidInfo()

        
    def run(self):
        self.mainloop()
    def exit(self):
        self.destroy()
        
        
    # person registration #########################################################################################################################################
    # person registration #########################################################################################################################################
    def OpenPersonReg(self):
        self.regFrame = ttk.Frame(self, borderwidth = 2, height=710, width=590)
        self.regFrame.place(x = 5 , y=5)
        labelframe = LabelFrame(self.regFrame, text="Person Registration", width=680, height=500)
        labelframe.pack(fill="both", expand="yes")
  
        self.entries = ['lastname', 'firstname', 'middlename','Suffix','Age','Gender','House#','Barangay','Town_city','Province','Contact#', 'Email_add', 'password']
        self.entryVal = []
        fromTop = 30
        for entry in self.entries:
            self.entry = ttk.Entry(self.regFrame,font=('bold', 12))
            self.entry.place(x = 250 , y = fromTop, height= 25, width=380)
            self.entryVal.append(self.entry)
            fromTop += 30
        
        self.labels = ['Last Name', 'First Name', 'Middle Name','Suffix','Age','Gender','House Number/ Street','Barangay','Town/City','Province','Contact Number', 'Email Address', 'Create Password']
        labelTop = 30
        for label in self.labels:
            self.label = ttk.Label(self.regFrame, text=f'{label}:' ,font=(12))
            self.label.place(x=50, y = labelTop)
            labelTop += 30
            # matapos mag fill up at mapupunta sa list ang info
        
        self.cancel = ttk.Button(self.regFrame, text='BACK',  command= self.registrationForm)
        self.cancel.place(x=250, y=465, width=125)
        
        self.clearPerson = ttk.Button(self.regFrame, text='CLEAR',  command= self.personClear)
        self.clearPerson.place(x=380, y=465, width=125)
        
        self.register = ttk.Button(self.regFrame, text='REGISTER',  command=self.PersonRegister) # gagamit tayo dito ng lambda
        self.register.place(x =510, y = 465, width=125)
        
    def PersonRegister(self):
        self.personInfo = {}
        for i, en in enumerate(self.entryVal):
            self.personInfo["info_{0}".format(i)] = en.get()
        if self.personInfo['info_0'] != '' and self.personInfo['info_1'] != '' and self.personInfo['info_4'] != '' and self.personInfo['info_5'] != '' and self.personInfo['info_1'] != '7'and self.personInfo['info_9'] != '' and self.personInfo['info_10'] != '' and self.personInfo['info_12'] != '':
            self.person = Person(self.personInfo['info_0'],self.personInfo['info_1'],self.personInfo['info_2'],self.personInfo['info_3'],self.personInfo['info_4'],self.personInfo['info_5'],
                                 self.personInfo['info_6'],self.personInfo['info_7'],self.personInfo['info_8'], self.personInfo['info_9'],self.personInfo['info_10'], self.personInfo['info_11'], self.personInfo['info_12'])
            self.person.register()
            self.person.SelectTable()
            DiaglogBox(self)
            self.registrationForm()
            
            for dlentry in self.entryVal:
                dlentry.delete(0, 'end')
        else:
            self.warningLabel = ttk.Label(self.regFrame, text='Necessary Information: Last Name, First Name, Age, Gender, Barangay, Town/City, Province, Password')
            self.warningLabel.place(x=120, y=420)
            
    def personClear(self):
        for dlentry in self.entryVal:
            dlentry.delete(0, 'end')
        
        
     ##############################################################################################################################################
###############################################################################################################################################
        
    def OpenEstForm(self):
        self.regFrame = ttk.Frame(self, borderwidth = 2, height=710, width=590)
        self.regFrame.place(x = 5 , y=5)
        labelframe = LabelFrame(self.regFrame, text="Establishment Registration Form", width=680, height=500)
        labelframe.pack(fill="both", expand="yes")
  
        self.entries = [ 'Establishment_Name',  'Barangay','Town_City','Province','Owner','Contact_Number', 'Email_Address','password']
        self.entryVal = []
        fromTop = 100
        for entry in self.entries:
            self.entry = ttk.Entry(self.regFrame)
            self.entry.place(x = 250 , y = fromTop, height= 25, width=380)

            self.entryVal.append(self.entry)
            fromTop += 30
        
        self.labels = ['Establishment Name','Barangay','Town/City','Province', 'Owner','Contact Number', 'Email Address','Create Password']
        labelTop = 100
        for label in self.labels:
            self.label = ttk.Label(self.regFrame, text=f'{label}:',font=(12))
            self.label.place(x=40, y = labelTop)
            labelTop += 30
            
        self.cancelEst = ttk.Button(self.regFrame, text='BACK',  command= self.registrationForm)
        self.cancelEst.place(x=250, y=465, width=125)
        
        self.clearEst = ttk.Button(self.regFrame, text='CLEAR',  command= self.registerEstClear)
        self.clearEst.place(x=380, y=465, width=125)
        
        self.clearReg = ttk.Button(self.regFrame, text='REGISTER',  command=self.registerEst) # gagamit tayo dito ng lambda
        self.clearReg.place(x =510, y = 465, width=125)
        
    def registerEst(self):
        self.personInfo = {}
        for i, en in enumerate(self.entryVal):
            self.personInfo["info_{0}".format(i)] = en.get()
        
        if self.personInfo['info_0'] != '' and self.personInfo['info_3'] != '' and self.personInfo['info_5'] != '' and self.personInfo['info_7'] != '':
            self.est = Establishment(self.personInfo['info_0'],self.personInfo['info_1'],self.personInfo['info_2'],self.personInfo['info_3'],self.personInfo['info_4'],self.personInfo['info_5'],
                                 self.personInfo['info_6'], self.personInfo['info_7'])
            self.est.register()
            self.est.SelectTable()
            Est_DiaglogBox(self)
            self.registrationForm()
            for dlentry in self.entryVal:
                dlentry.delete(0, 'end')
        else:
            self.warningLabel = ttk.Label(self.regFrame, text='Necessary Information: Establishment Name, Barangay, Town/City, Province, Your Password')
            self.warningLabel.place(x=220, y=400)
    def registerEstClear(self):
        for dlentry in self.entryVal:
            dlentry.delete(0, 'end')
        
            
    
            
class DiaglogBox(Toplevel, Database):
    cursor = None
    def __init__(self,master):
        Toplevel.__init__(self,master)
        Database.__init__(self)
        self.cursor = Database.cursor(self)
        
        self.geometry('500x380')
        self.title('Registration Done!')
        
        self._createLabels()
        self._button()
        
        style = ttk.Style()
        style.configure('FD.TLabel', font=('Helvetica', 12, 'bold'))
        
    def _createLabels(self):
        #'select ID,lastname,firstname,middlename,suffixname, age, gender, house_street,barangay,town_city,province,contactnum,email from  `registered_person`;'
        self.cursor.execute('select * FROM `registered_person` ORDER BY id DESC LIMIT 1;')

        for c in self.cursor:
           self.lastInfo = c
        
        self.youreIn = ttk.Label(self, text= 'Thank You!', style='FD.TLabel')  
        self.youreIn.place(x=80, y = 20)
        self.labels = ['Your ID','Last Name', 'First Name', 'Middle Name','Suffix','Age','Gender','House Number/ Street','Barangay','Town/City','Province','Contact Number', 'Email Address', 'Password']
        self.lblslist = []
        
        fromtop = 60
        for i, lbls in enumerate(self.labels):           
            self.lbls = ttk.Label(self, text=f'{lbls}: {self.lastInfo[i]} ', style='FD.TLabel')
            self.lbls.place(x=50, y = fromtop )
            self.lblslist.append(self.lbls)
            fromtop += 20
    def _button(self):
        self.exit = ttk.Button(self, text='GOT IT!', command=self._quit )
        self.exit.place(x=360, y =340)
        
    def _quit(self):
        self.destroy()
        
class Est_DiaglogBox(Toplevel, Database):
    cursor = None
    def __init__(self,master):
        Toplevel.__init__(self,master)
        Database.__init__(self)
        self.cursor = Database.cursor(self)
        
        self.geometry('500x380')
        self.title('Registration Done!')
        
        self._createLabels()
        self._button()
        
    def _createLabels(self):
        style = ttk.Style()
        style.configure('FD.TLabel', font=('Helvetica', 12, 'bold'))
        #'select ID,lastname,firstname,middlename,suffixname, age, gender, house_street,barangay,town_city,province,contactnum,email from  `registered_person`;'
        self.cursor.execute('select * FROM `registered_est` ORDER BY id DESC LIMIT 1;')
        self.filledInfo = []
        for c in self.cursor:
           self.lastInfo = c
        
        self.youreIn = ttk.Label(self, text= 'Thank You!', style='FD.TLabel')  
        self.youreIn.place(x=70, y = 20)
        self.labels = ['Establishment ID','Estblishment Name','barangay','Town city','Province', 'Owner','Contact Number','Email', 'Password']
        self.lblslist = []
        
        fromtop = 60
        for i, lbls in enumerate(self.labels):           
            self.lbls = ttk.Label(self, text=f'{lbls}: {self.lastInfo[i]} ',style='FD.TLabel')
            self.lbls.place(x=50, y = fromtop )
            self.lblslist.append(self.lbls)
            fromtop += 20
    def _button(self):
        self.exit = ttk.Button(self, text='GOT IT!', command=self._quit)
        self.exit.place(x=300, y =320)
        
    def _quit(self):
        self.destroy()

        
home = Home()
home.run()

      
