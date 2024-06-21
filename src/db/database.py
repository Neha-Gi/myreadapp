import psycopg as pg

#Singleton 
class Database(object):
    __instance = None

    def __new__(cls):
        if Database.__instance is None:
            Database.__instance = super().__new__(cls)
            Database.__instance.__init__()

        return Database.__instance.__conn    
    def __init__(self) -> None:
        self.__conn = pg.connect(
            #host = 'localhost'
            dbname = 'myreadapp', 
            user = 'postgres',
            password = 'postgres',
            #port = '5432'
        )