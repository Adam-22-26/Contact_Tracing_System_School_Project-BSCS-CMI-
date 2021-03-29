# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:51:31 2021


"""
from datetime import datetime

from mysqlconnector_tkinter import  Database
import mysql.connector as mysqldb

class Establishment(Database):
    cursor = None

    __table = 'registered_est'
    
    
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
                estname varchar(20) not null,
                barangay varchar(20) not null,
                town_city varchar(20) not null,
                province varchar(20) not null,
                estowner varchar(20) not null,
                contactnum varchar(11) unique not null,
                email varchar(20) unique not null,
                password varchar(20) unique not null
                );
            '''.format(self.__table))
            self.dateTime = str(datetime.today().strftime('%Y-%m-%d')).replace('-','')
            self.cursor.execute(f'ALTER TABLE {self.__table} AUTO_INCREMENT = {self.dateTime};')
            print('Table created:', self.__table)
        except mysqldb.Error as err:
            print('Error creating table:', err)
            
            
 
    def __init__(self,estname ,  barangay , town_city, province ,estowner, contactnum ,email, password):
        super().__init__()
        self.cursor = super().cursor()
        
        self.id = id
        
        self.estname = estname
        self.barangay = barangay
        self.town_city = town_city
        self.province = province 
        self.estowner = estowner
        self.contactnum = contactnum
        self.email = email
        self.password = password
                
        if self.__isTableExists():
            print('tables exists')
            
        else:
            self.__createTable()
                
    def register(self):
        """
        
        Insert data
        
        """

        
        try:

            self.cursor.execute("""
                                INSERT INTO {table} (estname,barangay, town_city, province,estowner, contactnum,email, password)
                                            VALUES ('{estname}',
                                                    '{barangay}',
                                                    '{town_city}', 
                                                    '{province}', 
                                                    '{estowner}',
                                                    '{contactnum}',
                                                    '{email}',
                                                    '{password}'
                                                    );
                """.format(
                    table=self.__table,
                    estname= self.estname,
                    barangay = self.barangay,
                    town_city = self.town_city,
                    province = self.province,
                    estowner = self.estowner,
                    contactnum = self.contactnum,
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
        
        self.cursor.execute('SELECT * FROM `registered_est`;') 
        for c in self.cursor:
            print(c)
            
#est = Establishment('Alex', 'puregold','masuso', 'Pandi', 'Bulacan', 1212,'Alexluismaniego@gmail.com', 'password')
#est.register()
#est.SelectTable()
#est.deleteDatabaseFromEarth()