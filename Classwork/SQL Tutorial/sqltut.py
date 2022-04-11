import sqlite3



conn = sqlite3.connect('example.db')

#create cursor
curs = conn.cursor()

curs.execute(""" CREATE TABLE IF NOT EXISTS example (
                lname text,
                fname text,
                age num,
                weight float,
                height float,
                bloodtype text,
                sex text

                
)""")




conn.commit()
conn.close()