from src.db.database import Database

#Insert reader qurey
def insert_data(username:str,title: str,first_name:str,last_name:str) -> tuple[str]:
    conn = Database()

    query = """
         Insert INTO project.reader(
         username,
         title,
         first_name,
         last_name

        ) VALUES(%s,%s,%s,%s) RETURNING *

"""

    with conn.cursor() as cursor:
        cursor.execute(query,(username,title,first_name,last_name))
        reader = cursor.fetchone()
        conn.commit()
        return reader