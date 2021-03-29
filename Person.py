# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:55:11 2021

@author: Adam-22-26
"""
from mysqlconnector_tkinter import  Database
import mysql.connector as mysqldb

class Person(Database):
    cursor = None

    __table = 'registered_person'
    
    
    def __isTableExists(self):
        """
        Check if table exists

        Returns
        -------
        bool
            Table exists.

        """
        self.cursor.execute('SHOW TABLES;')
        
        for table in self.cursor:
            if self.__table == table[0]:
                return True
        
        return False

    def __createTable(self):
        """
        Create table

        Returns
        -------
        None.

        """
        try:
            self.cursor.execute('''
                CREATE TABLE {0} (
                ID bigint(10) auto_increment primary key,
                lastname varchar(20) not null,
                firstname varchar(20) not null,
                middlename varchar(20),
                suffixname varchar(20),
                age varchar(20) not null,
                gender varchar(20) not null,
                house_street varchar(20) ,
                barangay varchar(20) ,
                town_city varchar(20) not null,
                province varchar(20) not null,
                contactnum varchar(20)  not null,
                email varchar(20)  not null,
                password varchar(20) unique not null
                    
                );
            '''.format(self.__table))
            self.cursor.execute(f'ALTER TABLE {self.__table} AUTO_INCREMENT = 21000;')
            print('Table created:', self.__table)
        except mysqldb.Error as err:
            print('Error creating table:', err)
            
            

    def __init__(self,lastname , firstname, middlename, suffixname , age, gender, house_num_street ,
                 barangay ,town_city,province,contact_num, email_add, password):
        super().__init__()
        self.cursor = super().cursor()
        
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.suffixname = suffixname
        self.age = age
        self.gender = gender 
        self.house_street = house_num_street
        self.barangay = barangay
        self.town_city = town_city
        self.province = province
        self.contactnum = contact_num
        self.email = email_add
        self.password =password
        
        
        
        if self.__isTableExists():
            #self.cursor.execute(f'ALTER TABLE {self.__table} AUTO_INCREMENT = 21000;')
            print('tables exists')
            
        else:
            self.__createTable()
        
        
        
        
        
    def register(self):
        """
        
        Insert data
        
        """

        
        try:

            self.cursor.execute("""
                                INSERT INTO {table} (lastname,firstname,middlename,suffixname, age, gender, house_street,barangay,town_city,province,contactnum,email,password)
                                            VALUES ('{lastname}',
                                                    '{firstname}',
                                                    '{middlename}', 
                                                    '{suffixname}', 
                                                    '{age}', 
                                                    '{gender}',
                                                    '{house_street}',
                                                    '{barangay}',
                                                    '{town_city}',
                                                    '{province}',
                                                    '{contactnum}',
                                                    '{email}',
                                                    '{password}');
                """.format(
                    table=self.__table,
                    lastname= self.lastname,
                    firstname = self.firstname,
                    middlename= self.middlename,
                    suffixname = self.suffixname,
                    age = self.age,
                    gender = self.gender,
                    house_street = self.house_street,
                    barangay = self.barangay,
                    town_city = self.town_city,
                    province  = self.province,
                    contactnum  = self.contactnum,
                    email = self.email,
                    password = self.password))
            ## Save changes
            super().update()
            print('complete inserting')
        except mysqldb.Error as err:
            pass
            print(f'Error inserting {self.__table}:', err)
            
    def remove(self):

        try:
            self.cursor.execute("""
                DELETE FROM {table} WHERE `id` = {id}
                """.format(
                    table=self.__table,
                    id=self.id
                )
            )
            print(f'Person removed from database #{self.id}')
            
            ## Save changes
            super().update()
        except mysqldb.Error as err:
            print('Error removing person:', err)
            
    def deleteDatabaseFromEarth(self):
        try:
            self.cursor.execute('drop database Contact_tracing01010;')
            print('deleted database kahit ano yun')
        except mysqldb.Error as error:
            print('error delete you from Earth! ', error)
    
    def SelectTable(self):
        
        self.cursor.execute('SELECT * FROM registered_person;') 
        for c in self.cursor:
            print(c)

#person = Person('Marcaida', 'Firstname','Compio','C', 'Jr.', 'Male', 'blk 30 lot 30', 'masuso', 'Pandi', 'Bulacan', 9120090952,'adamcompiomarcaida@gmail.com')
#person.SelectTable()
#person.deleteDatabaseFromEarth()
    