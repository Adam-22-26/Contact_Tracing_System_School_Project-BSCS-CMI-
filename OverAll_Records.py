from tkinter import *
from tkinter import ttk
from mysqlconnector_tkinter import Database
import mysql.connector as mysqldb
from tkcalendar import DateEntry
from datetime import datetime

class ShowAll_Data(Tk, Database):
    _curosr = None
    def __init__(self):
        Tk.__init__(self)
        Database.__init__(self)
        self._cursor = Database.cursor(self)
        
        self.geometry('1155x600')
        self.title('Database Records')       
                
        self.canvas = Canvas(self)
        self.canvas.place(relx=0, rely=0, relheight=1, relwidth=1, x=5,y= 50)
        self.frame =ttk.Frame(self.canvas)
        
        
        self.frame.bind('<Configure>', self.on_configure)
        self.canvas.create_window(0, 0, window = self.frame)
        
        self.scrollbar = ttk.Scrollbar(self, command=self.canvas.yview)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.search = ttk.Entry(self)
        self.search.place(x=10,y=10, height = 25 )
        
        self.searchBtn = ttk.Button(self, text='Search', command=self._searchResult)
        self.searchBtn.place(x=150,y =9)
        self._data()
        
        self.description = ttk.Label(self, text= 'Search example Date (yyyy-mm-dd) ')
        self.description.place(x=250, y = 9)
        
    def on_configure(self, even):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
        
    def run(self):
        self.mainloop()
        
    def _data(self):

        try:
            self._cursor.execute("""
                                 select   `registered_person`.`id`, firstname, registered_person.lastname, age, gender,`registered_person`.`barangay`,
                                 `registered_person`.province, `registered_person`.contactnum,`registered_person`.email,estname, date
                                 from `logs` inner join `registered_person` on `logs`.`registered_personID` = `registered_person`.`ID`
                                             inner join `registered_est` on`logs`.`ID_from_est1` = `registered_est`.`ID`
                                 """)
            self.__data = []
            for data in self._cursor:
                if str(data[10]) == datetime.today().strftime('%Y-%m-%d'):
                    self.__data.append(data)
                    
                    
            self.totalrows = len(self.__data)
            self.totalcolumns = len(self.__data[0])
            print(self.totalrows)
            for i in range(self.totalrows):
                for j in range(self.totalcolumns):                        
                    self.ent = ttk.Entry(self.frame, width = 16)
                    self.ent.grid(row=i, column=j )
                    self.ent.insert('end', self.__data[i][j])
                    self.ent.configure(state='disabled')

            
        except mysqldb.Error as error:
            print('Error Joining',error)
            
    def _searchByDate(self):

        
        self.lblDate = ttk.Label(self, text = 'Search By Date')
        self.lblDate.place(x=250, y =9)
        self.date = DateEntry(self, width=12, height= 25, year=2021, month=3, day=23, background='darkblue', foreground='white', borderwidth=2)
        self.date.place(x= 350, y = 9)
        self.dateDB = self.date.get().replace('/', '-')
        print(self.dateDB)
    
    def _searchResult(self):
        #self._searchByDate()
        
        try:
            self._cursor.execute("""
                                 select   `registered_person`.`id`, firstname, registered_person.lastname, age, gender,`registered_person`.`barangay`,
                                 `registered_person`.province, `registered_person`.contactnum,`registered_person`.email,estname, date
                                 from `logs` inner join `registered_person` on `logs`.`registered_personID` = `registered_person`.`ID`
                                             inner join `registered_est` on`logs`.`ID_from_est1` = `registered_est`.`ID`
                                 """)
            self.__data = []
            try:
                for data in self._cursor:
                    for dt in data:
                        if str(dt).lower() == str(self.search.get()).lower():
                            self.__data.append(data)            
            
                    
                self.totalrows = len(self.__data)
                self.totalcolumns = len(self.__data[0])
                print(self.totalrows)
                for i in range(self.totalrows):
                    for j in range(self.totalcolumns):                        
                        self.ent = ttk.Entry(self.frame, width = 16)
                        self.ent.grid(row=i, column=j )
                        self.ent.insert('end', self.__data[i][j])
                        self.ent.configure(state='disabled')
            except IndexError:
                print('Not found')

            
        except mysqldb.Error as error:
            print('Error Joining',error)

class SignIn(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('300x150')
        self.title('log in')
        
        self.button_entry()
    def button_entry(self):
        self.userlabel = ttk.Label(self, text='Username:')
        self.userlabel.place(x=20, y= 30)
        self.username =ttk.Entry(self, font=('Arial', 11,'bold'))
        self.username.place(x=110, y=30)
        
        self.passlabel = ttk.Label(self, text='Password:')
        self.passlabel.place(x=20, y= 60)
        self.password = ttk.Entry(self, font=('Arial', 11,'bold'))
        self.password.configure(show='#')
        self.password.place(x=110, y=60)
        
        self.login = ttk.Button(self, text='Log in',  command=self._mainWindow)
        self.login.place(x=200, y= 100)        
        
    def _mainWindow(self):
        records =ShowAll_Data()
        self.destroy()
        records.run()
        
        
    def run(self):
        self.mainloop()

signIn = SignIn()
signIn.run()

