

import mysql.connector as mysqldb

class Database:
    
    """
    Database name
    """
    __database = 'breakout4db'
    
    """
    MySQL cursor
    """
    cursor = None
    
    def __mydatabase(self):
        return self.__database
    
    def __isDbExists(self):
        """
        Check if database exists
        
        Returns
        -------
        bool
            Database exists

        """
        self.cursor.execute('SHOW DATABASES')
        
        for database in self.cursor:
            if self.__database == database[0]:
                return True
        
        return False

    def __createDb(self):
        """
        Create database

        Returns
        -------
        None.

        """
        try:
            self.cursor.execute(f'CREATE DATABASE {self.__database};')
            print('Database created:', self.__database)
        except mysqldb.Error as err:
            pass
            #print('Error creating database:', err)
            
    def __useDb(self):
        """
        Use database

        Returns
        -------
        None.

        """
        try:
            self.cursor.execute(f'USE {self.__database};')
        except mysqldb.Error as err:
            print('Error using database:', err)

    def __init__(self):
        """
        Class constructor

        Returns
        -------
        None.

        """
        self.connection = mysqldb.connect(
            host='db4free.net',
            user='breakout4',
            password='adamalexaron',
            buffered=True # Prevent unbuffered mysql connection
        )
        
        self.cursor = self.connection.cursor()

        if self.__isDbExists():
            print("Database already exists")
        else:
            self.__createDb()
            
        self.__useDb()
            
    def cursor(self):
        """
        Database cursor

        Returns
        -------
        object
            MySQL cursor.

        """
        return self.cursor
    
    def update(self):
        """
        
        Update database
        
        """
        self.connection.commit()