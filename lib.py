import db
from datetime import date,timedelta
database=db.get_db_connection()
cur=database.cursor()
def add_book(title, author, year,avail_status):
    database=db.get_db_connection()
    cur=database.cursor()
    cur.execute(
        "INSERT INTO books(title,author,year,avail_status) values(?,?,?,?)",
        (title, author, year,avail_status))
    print("Book added successfully !!!")
    database.commit()
    database.close()
def view_available_books():
    database=db.get_db_connection()
    cur=database.cursor()
    cur.execute(
        "SELECT * FROM books where avail_status>0")
    row=cur.fetchall()
    print("Available books are: ")
    for i in row:
        print(i)
    database.close()
def borrow_book(book_id, borrower_name):
    database=db.get_db_connection()
    cur=database.cursor()
    cur.execute("select avail_status from books where book_id=?",(book_id,))
    data=cur.fetchone()
    if data is None:
        print("Book ID not found.")
        return
    avail_status=data[0]
    if avail_status>0:
        borrow_date=date.today()
        due_date=borrow_date+timedelta(days=6)
        cur.execute(
            "UPDATE books SET avail_status=avail_status-1 where book_id= ?",(book_id,))
        cur.execute(
            "INSERT INTO borrowed(book_id,borrower_name,borrow_date,due_date) values(?,?,?,?)",(book_id, borrower_name,borrow_date,due_date))
        database.commit()
        print("Book borrowed successfully")
    else:
        print("sorry, Book is unavailable")
    
    database.close()
def return_book(book_id):
    database=db.get_db_connection()
    cur=database.cursor()
    cur.execute("select * from borrowed where book_id=? and return_date is null",(book_id,))
    data=cur.fetchone()
    if not data:
        print("Invalid borrow id or book already returned !!!")
    else:
        return_date=date.today()
        cur.execute("update books set avail_status=avail_status+1 where book_id=?",(book_id,))
        cur.execute("update borrowed set return_date=? where book_id=? and return_date is NULL",(return_date,book_id))
        database.commit()
        print("Return successfully!!")
    database.close()
def show_borrowed_books():
    database=db.get_db_connection()
    cur=database.cursor()
    cur.execute(
        "SELECT * FROM borrowed where return_date is NULL")
    rows=cur.fetchall()
    if not rows:
        print("No books are borrowed")
    else:  
        print("Borrowed books are: ")
        for i in rows:   
            print(i)
    database.close()