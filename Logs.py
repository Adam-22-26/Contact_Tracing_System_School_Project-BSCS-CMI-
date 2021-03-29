
from mysqlconnector_tkinter import  Database
import mysql.connector as mysqldb

class Est_Logs(Database):
    cursor = None

    __table = 'logs'
    __est_ID = 0
    
    
    
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
        # `time` time not null,
        try:
            self.cursor.execute('''
                CREATE TABLE {0} (
                ID bigint(6) zerofill auto_increment primary key,
                `date` date not null,
                
                registered_personID bigint(10) not null,
                ID_from_est1 bigint(10) not null,
                
                FOREIGN KEY (`registered_personID`) REFERENCES `registered_person`(`ID`),
                FOREIGN KEY (`ID_from_est1`) REFERENCES `registered_est`(`ID`)
                );
            '''.format(self.__table))
            print('Table created:', self.__table)
        except mysqldb.Error as err:
            print('Error creating table:', err)
            
            

    def __init__(self,registered_personID):
        Database.__init__(self)
        self.cursor = Database.cursor(self)
        
        self.id = id
        self.registered_personID = registered_personID 

        
        
        if self.__isTableExists():
            print('tables exists')
            
        else:
            self.__createTable()
        
        
        
    def est_id(self, id):
        
        self.__est_ID = id
        print(self.__est_ID)
        
    def register(self):
        """
        
        Insert data
        
        """

        
        try:

            self.cursor.execute("""
                                INSERT INTO {table} (date,registered_personID,ID_from_est1)
                                            VALUES (current_date(),
                                                    '{registered_personID}',
                                                    '{ID_from_est1}');
                """.format(
                    table=self.__table,
                    registered_personID = self.registered_personID,
                    ID_from_est1= self.__est_ID
                    ))
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
        
        self.cursor.execute('SELECT * FROM logs;') 
        for c in self.cursor:
            print(c)
            


#logs.deleteDatabaseFromEarth()
    