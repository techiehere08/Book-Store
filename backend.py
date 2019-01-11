import sqlite3
def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book  (Id INTEGER PRIMARY KEY,Title text,Author text,Year INTEGER,ISBN INTEGER)")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book ")
    all=cur.fetchall()
    conn.close()
    return all



def entry(t,a,y,i):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(t,a,y,i))
    conn.commit()
    conn.close()

def search(t="",a="",y="",i=""):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(t,a,y,i))
        all = cur.fetchall()
        conn.close()
        return all

def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE Id=? ",(id,))
    conn.commit()
    conn.close()

def update(id,t,a,y,i):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("update book set Title=?,Author=?,Year=?,ISBN=? where id=?",(t,a,y,i,id))
    conn.commit()
    conn.close()

connect()



