import db
from lib import *
from datetime import date
def display_menu():
    print("\n\n<----Library---->\n")
    print("1. Add Book")
    print("2. View Available Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Borrowed Books")
    print("6. Exit")
    
if __name__=="__main__":
    db.get_db_connection()
    db.create_tables()
    while(True):
        display_menu()
        choice=input("Select your choice:-- ")
        if choice=="1":
            title=input("Enter book title: ")
            author=input("Enter name of the author: ")
            year=int(input("Enter year: "))
            avail_copies=int(input("Enter no of copies available: "))
            add_book(title,author,year,avail_copies)
        elif choice=="2":
            view_available_books()
        elif choice=="3":
            book_id=int(input("Enter book id: "))
            borrower_name=input("Enter the name: ")
            borrow_book(book_id, borrower_name)
        elif choice=="4":
            book_id=int(input("Enter book id: "))
            return_book(book_id)
        elif choice=="5":
            show_borrowed_books()
        elif choice=="6":
            print("Exiting program")
            break
        else:
            print("Invalid input")

            
        
        