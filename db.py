import sqlite3

def get_db_connection():
    database=sqlite3.connect("library.db")
    return database
def create_tables():
    db=get_db_connection()
    cur=db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id integer primary key autoincrement,
        title varchar(50), 
        author varchar(50),
        year integer,
        avail_status integer)""")
    cur.execute("""
                CREATE TABLE IF NOT EXISTS borrowed(
                    borrow_id integer PRIMARY KEY AUTOINCREMENT,
                    book_id integer,
                    borrower_name varchar(50),
                    borrow_date date not null,
                    due_date date,
                    return_date date)""")
    db.commit()
    db.close()
    