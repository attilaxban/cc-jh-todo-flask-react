import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)



conn = psycopg2.connect(
        host="localhost",
        database="todo_db",
        user=os.getenv('USER_NAME'),
        password=os.getenv('PASSWORD')
)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS todos;')
cur.execute('''CREATE TABLE todos (
                id serial PRIMARY KEY,
                todo varchar (150) NOT NULL,
                date_added date DEFAULT CURRENT_TIMESTAMP,
                isFinished BOOLEAN DEFAULT FALSE
              );'''
            )

cur.execute(
    'INSERT INTO todos (todo) VALUES (%s)',
    ('Learn Flask',)
)
conn.commit()
cur.close()
conn.close()
