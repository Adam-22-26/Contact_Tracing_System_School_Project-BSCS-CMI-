from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time as delay
import mysql.connector as mysqldb
from mysqlconnector_tkinter import  Database
from Logs import Est_Logs
from datetime import datetime




class HostEstblishment(Tk, Database):
    _cursor = None
    def __init__(self):
        Database.__init__(self)
        Tk.__init__(self)
        self._cursor = Database.cursor(self)
        #ceate window
        self.geometry('700x520+0+0')
        self.title('Contact-Tracing-System')
        self.configure(bg='CadetBlue3')
        self.resizable(False,False)      
        self.image()
        self._Welcome()
        self.register()
        
        self.styleIdEntry = ttk.Style()
        self.styleIdEntry.configure('TEntry',font=('bold', 25))
        
        
        style = ttk.Style()
        style.configure('welcome.TLabel',font= ('Helvetica', 15, 'bold'))
        style.configure('enterid.TLabel',font= ('Helvetica', 12, 'bold'))
        style.configure('enter.TButton',foreground='black', background='DeepSkyBlue2')
        
        self.est_logFirst()
        
        
        
    def image(self):
        imgp = Image.open('./c2.png')
        self.imgresized = imgp.resize((685,250), Image.ANTIALIAS)
        self.image00 = ImageTk.PhotoImage(self.imgresized)
        self.label = ttk.Label(self, image=self.image00)
        self.label.place(x=5, y=5)
        
    def _Welcome(self):
        
        
        self.frameLeft = ttk.Frame(self,width = 340, height = 250)
        self.frameLeft.place(x=5, y = 265)
        labelframe = ttk.LabelFrame(self.frameLeft, text="Log In", width=340, height=250)
        labelframe.pack(fill="both", expand="yes")
               
        self.frameRight = ttk.Frame(self, width = 330, height = 340)
        self.frameRight.place(x=355, y =265)
        labelframe = ttk.LabelFrame(self.frameRight, text="Verify if its you", width=340, height=250)
        labelframe.pack(fill="both", expand="yes")
        
        
    def est_logFirst(self):
        style = ttk.Style()
        style.configure('label.TLabel', font=('Helvetica', 12, 'bold'))

        
        self.login_Label = ttk.Label(self.frameLeft, text= 'ID:',style='label.TLabel')
        self.login_Label.place(x=10, y = 100)
        self.pass_Label = ttk.Label(self.frameLeft, text='PASSWORD:', style='label.TLabel')
        self.pass_Label.place(x=10, y =155)
             
        self.estLogin = ttk.Entry(self.frameLeft, justify='center', font=('Helvitica', 12, 'bold'))
        self.estLogin.place(x=120, y=105,  width=200, height=30)
        
        self.est_pass = ttk.Entry(self.frameLeft, justify='center', font=('Helvitica', 12, 'bold'))
        self.est_pass.place(x=120, y=155,width=200, height=30)
        self.est_pass.configure(show='#')   
        self.est_Enter = ttk.Button(self.frameLeft, text='ENTER',style='enter.TButton', command=self._logIn)
        self.est_Enter.place(x=10, y=210, width=320, height=30)

    
    def _logIn(self):
        
        try:
            self._cursor.execute('select id, password, estname from registered_est;')

            for idPass in self._cursor:
                if int(idPass[0])  == int(self.estLogin.get()) and str(idPass[1]) == str(self.est_pass.get()):
                    self.estname = idPass[2]
                    self.estID = idPass[0]
                    print(idPass[0], idPass[1], idPass[2])
                    
             
                    self.welcome = ttk.Label(self.frameLeft,text=f'Welcome to: {self.estname}', style='welcome.TLabel')
                    self.welcome.place(x=10, y = 20)

                    self.idLabel = ttk.Label(self.frameLeft, text='Enter your  ID: ', style= 'enterid.TLabel')
                    self.idLabel.place(x=10, y=50)
                    
                    self.idEntry = ttk.Entry(self.frameLeft,justify='center',font=('Arial', 12, 'bold'))
                    self.idEntry.place(x=10, y =80 , width = 320, height = 30)                    

                    self.passlabel = ttk.Label(self.frameLeft, text='PASSWORD: ', style= 'enterid.TLabel')
                    self.passlabel.place(x=10, y=120)
                    
                    self.passEnt = ttk.Entry(self.frameLeft,justify='center',font=('Arial', 12, 'bold'))
                    self.passEnt.place(x=10, y =150 , width = 320, height = 30)
                    self.passEnt.configure(show='#')
                    
                    self.enter = ttk.Button(self.frameLeft, text ='ENTER',command=  self.getEntry,style='enter.TButton')
                    self.enter.place(x=10, y =210, width = 320, height = 30)
                    self.login_Label.destroy()
                    self.pass_Label.destroy()
                    self.estLogin.destroy()
                    self.est_pass.destroy()
                    self.est_Enter.destroy()   
        except mysqldb.Error as err:
            print('error loggin in Estabishment', err)
    
        
    def register(self):

        
        #self.registerBtn = ttk.Button(self.frameRight, text='Next', command=self.Label_delete, style='enter.TButton')
        #self.registerBtn.place(x=10, y=210,width = 270, height = 30)
        
        self.registerBtn = ttk.Button(self.frameRight, text='Exit', command=self.exit, style='enter.TButton')
        self.registerBtn.place(x=10, y=210,width = 320, height = 30)
        
        
    def returnInfo(self, remaining=None):
        style = ttk.Style()
        style.configure('yourIn.TLabel', font=('Helvetica', 17, 'bold'), justify='center')
        style.configure('name.TLabel', font=('Helvetica', 20, 'bold'), justify='center')
        
        self.youreIn = ttk.Label(self.frameRight, text='', style='yourIn.TLabel')  
        self.youreIn.place(x=100, y = 50)
        self.name = ttk.Label(self.frameRight, style='name.TLabel')
        self.name.place(x = 20, y = 155)
        
        self.remaining = 0
        if remaining is not None:
            self.remaining = remaining
        
        if self.remaining <= 0:
            self.youreIn.configure(text='                                  ')
            self.name.configure(text='                                     ')
            self.configure(bg='CadetBlue3')
        else:
            self.youreIn.configure(text= 'You Are In!')
            self.name.configure(text = f'{self.validName}')
            self.configure(bg='PaleGreen3')
            self.remaining = self.remaining - 1
            self.after(2000, self.returnInfo)

    def warning(self, remain = None):
        self.remain = 0
        if remain is not None:
            self.remain = remain 
        if self.remain <= 0:
            self.configure(bg='CadetBlue3')
        else:
            self.configure(bg='red')
            self.remain = self.remain - 1
            self.after(1000, self.warning)
        
        
        
            
    def getEntry(self):     
        self._id = self.idEntry.get()
        try:
            self._cursor.execute('select id, password,firstname, lastname from `registered_person`')
            self.fullname = []
            for id in self._cursor:
                if self._id == str(id[0]) and self._id != '' and str(self.passEnt.get()) == str(id[1]):
                    self.fullname.append(id[2:])
                    
                    logs = Est_Logs(self._id)
                    logs.est_id(self.estID)
                    logs.register()
                    logs.SelectTable()
                    self.idEntry.delete(0,'end')
                    self.passEnt.delete(0, 'end')
                    
                    self.flname = [' '.join(name) for name in self.fullname]
                    self.validName = ' '.join(self.flname)
                    self.returnInfo(2)
                else:
                  self.warning(1)
                            
                        
        except mysqldb.Error as err:
            print('Cannot find ID', err)

                
        
    def exit(self):
        self.destroy()
        
    def run(self):
        self.mainloop()






est = HostEstblishment()
est.run()
        

        
