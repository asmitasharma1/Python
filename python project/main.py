import sqlite3
import os

conn = sqlite3.connect("library.sqlite")
cur = conn.cursor()

create_script = '''
CREATE TABLE library (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(40) NOT NULL,
    author_name VARCHAR(40) NOT NULL,
    borrowed VARCHAR(6))
    '''

 #RUN ONLY ONCE
 #cur.execute(create_script)

print("       WELCOME TO THE LIBRARY MANAGEMENT SYSTEM       ")
print("------------------------------------------------------")
print("Enter 1.To Display\n")
print("Enter 2.To Borrow a book\n")
print("Enter 3.To Return book\n")
print("Enter 4.To Add a book\n")
print("Enter 4.To exit\n")

choice = int(input("Enter your choice: "))

try:
    
    if (choice != 1 and choice != 2 and choice != 3 and choice != 4):
        raise ValueError
    
    else:
        
        if (choice == 1):
            book_display_script = '''SELECT * FROM library'''
            book_dump = cur.execute(book_display_script)
            print("The details of book are: \n")
            print("BOOK ID\t BOOK NAME\t AUTHOR NAME\t BORROWED")
            for books in book_dump:
                print(f"{books[0]}\t{books[1]}\t{books[2]}\t{books[3]}")

        elif (choice == 2):
            book_id = int(
                input("Enter the book id which you want to borrow: "))
            filterScript = f'''
            UPDATE library SET borrowed = "YES" WHERE book_id = {book_id} AND borrowed = "NO"'''
            cur.execute(filterScript)
            print("Successfully borrowed the book")

        elif (choice == 3):
            book_id = int(
                input("Enter the book id which you want to return: "))
            filterScript = f'''
            UPDATE library SET borrowed = "NO" WHERE book_id = {book_id} AND borrowed ="YES"'''
            cur.execute(filterScript)

        elif (choice == 4):
            numberOfBooks = int(input("Enter the number of books to enter: "))
            
            for i in range(numberOfBooks):
                book_id = int(input("enter the book id: "))
                book_name = input("Enter the book name: ")
                author_name = input("Enter the author name: ")
                borrowed = "NO"
                insert_script = '''INSERT INTO library VALUES (?,?,?,?)'''
                cur.execute(insert_script, (book_id, book_name, author_name, borrowed))
                print("\n")        

#Exception Handling
except ValueError:
    print("Invalid choice")
conn.commit()
conn.close()
