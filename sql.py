from os import name
import sqlite3

conn = sqlite3.connect('Images.db')

cursor = conn.cursor()

#cursor.execute("""DROP TABLE IF EXISTS files""")
cursor.execute("""CREATE TABLE IF NOT EXISTS files (
    filename TEXT NOT NULL,
    img BLOB NOT NULL
    )"""
)


conn.commit() 

conn.close()

#add entry to database with given name/bytes
def addInfo(name, bytes):
    conn = sqlite3.connect('Images.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO files VALUES (?, ?)""", [name,bytes])
    conn.commit()
    conn.close()
    print("Successfuly Added as {}!".format(name))

#method to return tuple of info for given name (takes name as arg):
def getInfo(name):
    conn = sqlite3.connect('Images.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM files WHERE filename=?""", [name])
    b = cursor.fetchall()
    conn.close()
    return b

#Print all file names included in database
def getFilenames():
    conn = sqlite3.connect('Images.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT filename FROM files""")
    name_list = cursor.fetchall()
    conn.close()
    if name_list:
        for i in name_list:
            print(i[0])
    else:
        print("There are no files added.")



