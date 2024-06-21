import psycopg as pg

#Singleton 
class Database:
    def __init__(self) -> None:
        self.__conn = pg.connect(
            #host = 'localhost'
            dbname = 'myreadapp', 
            user = 'postgres',
            password = 'postgres',
            #port = '5432'
        )