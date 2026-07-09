import os
import sqlite3

os.chdir("D:\\Ashwini studies\\Data science Bootcamp UNSW\\Tasks\\task py files\\capston projects\\bookstore project")


def connect_db():
    try:
        # craete database called ebookstore and established connection
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        return db, cursor
    except Exception as e:
        raise e

 # creates author and book tables if not already exist


def create_table():
    try:
        # creates author and book tables if not already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS author(
                id INTEGER PRIMARY KEY,
                name TEXT,
                country TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY,
                title TEXT,
                authorID INTEGER,
                qty INTEGER
            )
        ''')

        db.commit()
    except Exception as e:
        db.rollback()
        raise e


# Add new book to the database


def enter_book():
    # print("Add new book to database")
    try:
        id = int(input("Please enter book id:"))
        author_ID = int(input("Please enter author id:"))

        cursor.execute('''SELECT * FROM book WHERE ID= ?''', (id,))
        book = cursor.fetchone()
        if book is None:
            cursor.execute(
                '''SELECT * FROM author WHERE ID= ?''', (author_ID,))
            author = cursor.fetchone()
            if author is None:
                author_name = input("Please enter author name:")
                country = input("Please enter country:")
                cursor.execute('''
                    INSERT INTO author(id, name, country)
                    VALUES (?, ?, ?)
                    ''', (author_ID, author_name, country))

                title = input("Please enter book title:")
                qty = int(input("Please enter book quantity:"))
                cursor.execute('''
                    INSERT INTO book(id, title, authorID, qty)
                    VALUES (?, ?, ?, ?)
                    ''', (id, title, author_ID, qty))
            else:
                print("Author id is already present")
                title = input("Please enter book title:")
                qty = int(input("Please enter book quantity:"))
                cursor.execute('''
                        INSERT INTO book(id, title, authorID, qty)
                        VALUES (?, ?, ?, ?)
                        ''', (id, title, author[0], qty))
        else:
            print("Book id is already present")
            return

        db.commit()
        print("Book is enterd Successfully")

    except Exception as e:
        db.rollback()
        raise e


# Update existing books from database


def update_book():
    """
       Update existing book from database

    """

    try:
        # print("update existing book from database")
        id = int(input("Please enter book id:"))

        cursor.execute('''SELECT * FROM book WHERE ID= ?''', (id,))
        book = cursor.fetchone()
        if book is None:
            print("Cant find the Book")
            return
        else:
            book_id = book[0]
            book_title = book[1]
            author_id = book[2]
            qty = book[3]

            # print(book_id)
            # print(book_title)
            # print(author_id)
            # print(qty)

            cursor.execute(
                '''SELECT * FROM author WHERE ID= ?''', (author_id,))
            author = cursor.fetchone()
            if author is None:
                return
            else:
                autor_name = author[1]
                autor_country = author[2]

                # print(autor_name)
                # print(autor_country)

            is_update_title = input(
                "Do you want to update the title (yes or no):")
            updated_book_title = book_title
            # print(is_update_title.strip().lower())
            if is_update_title.strip().lower() == "yes":
                updated_book_title = input("Please enter the new  book title:")
                print(updated_book_title)

            is_update_qty = input(
                "Do you want to update quantity (yes or no):")
            updated_book_qty = qty
            if is_update_qty.strip().lower() == "yes":
                updated_book_qty = int(
                    input("Please enter the updated quantity:"))
                # print(updated_book_qty)

            is_upadate_author_name = input(
                "Do you want to update Author Name (yes or no):")
            updated_author_name = autor_name
            if is_upadate_author_name.strip().lower() == "yes":
                updated_author_name = input(
                    "Please enter the new Author Name :")

            is_upadate_author_country = input(
                "Do you want to update Author country (yes or no):")
            updated_author_country = autor_country
            if is_upadate_author_country.strip().lower() == "yes":
                updated_author_country = input(
                    "Please enter the new Author country :")

            cursor.execute('''
                    UPDATE book
                    SET title = ? , qty= ?  
                    WHERE id= ?
                    ''', (updated_book_title, updated_book_qty, book_id))

            cursor.execute('''
                    UPDATE author
                    SET name = ? , country= ?
                    WHERE id=?
                    ''', (updated_author_name, updated_author_country, author_id))

            is_upadate_author_Id = input(
                "Do you want to update Author ID (yes or no):")
            updated_author_ID = author_id
            if is_upadate_author_Id.strip().lower() == "yes":
                new_author_ID = int(input("Please enter the new Author Id :"))

                cursor.execute("SELECT * FROM author WHERE ID= ? ",
                               (new_author_ID,))
                author = cursor.fetchone()
                if author is None:
                    print("This Author number is not stored in database")
                    print("ua- update existing authors author Id")
                    print("na - To enter new author please ")

                    author_choice = input(
                        "Plese enter your choice from the menu:")
                    if author_choice.strip().lower() == "ua":
                        updated_author_ID = new_author_ID
                        # print(book_id)
                        # print(author_id)
                        cursor.execute('''
                                    UPDATE book
                                    SET authorID = ?
                                    WHERE id= ?
                                    ''', (updated_author_ID, book_id))

                        cursor.execute('''
                                    UPDATE author
                                    SET id = ? 
                                    WHERE id=?
                                    ''', (updated_author_ID, author_id))

                    else:
                        updated_author_ID = new_author_ID
                        author_name = input("Please enter author name:")
                        country = input("Please enter country:")
                        cursor.execute('''
                                    UPDATE book
                                    SET authorID = ?
                                    WHERE id= ?
                                    ''', (updated_author_ID, book_id))

                        cursor.execute('''
                            INSERT INTO author(id, name, country)
                            VALUES (?, ?, ?)
                            ''', (updated_author_ID, author_name, country))

                else:
                    print("This Author id is already present")
                    print(
                        f"Author Id : {author[0]} : Author Name : {author[1]} : Author Country : {author[2]} ")
                    auth_choice = input(
                        "Do you want to choose the exisitng author (Yes or No)")
                    if auth_choice.strip().lower() == 'yes':
                        updated_author_ID = author[0]

                        cursor.execute('''
                                UPDATE book
                                SET authorID = ?
                                WHERE id= ?
                                ''', (updated_author_ID, book_id))

                       # print("Book and Author information is updated")
                    else:
                        return
        db.commit()
        print("Book and Author information is updated")
    except Exception as e:
        db.rollback()
        raise e

# delete existing books from database


def delete_book():
    try:
       # print("Delete existing book from database")
        book_id = int(input("Please enter the book Id:"))
        cursor.execute('''SELECT * FROM book WHERE id= ?''', (book_id,))
        book = cursor.fetchone()
        if book is None:
            print("This Book Id is not present in the book table")
            return
        else:
            book_id = book[0]
            author_id = book[2]
            cursor.execute(
                '''SELECT * FROM book WHERE ID != ? AND authorID = ?''', (book_id, author_id))
            book = cursor.fetchone()
            if book:
                cursor.execute(
                    ''' DELETE FROM book WHERE id= ?''', (book_id,))
            else:
                cursor.execute(
                    ''' DELETE FROM book WHERE id= ?''', (book_id,))
                cursor.execute(
                    ''' DELETE FROM author WHERE id= ?''', (author_id,))
        db.commit()
        print("Book and Author information is Deleted")
    except Exception as e:
        db.rollback()
        raise e


# search existing books from database


def search_book():
    try:
        # print("Search existing book from database")
        book_id = int(input("Please enter the book Id:"))
        cursor.execute(''' SELECT
                    book.id,
                    book.title,
                    book.qty,
                    book.authorID,
                    author.name,
                    author.country
                    FROM book
                    INNER JOIN author
                    ON book.authorID = author.id
                    WHERE book.id = ?''', (book_id,))
        books = cursor.fetchall()
        for book in books:
            (id, title, qty, authorID, name, country) = book
            print(f" Book Id: {id}")
            print(f" Book Title:{title}")
            print(f" Book Qty: {qty}")
            print(f" Author Id: {authorID}")
            print(f" Auther Name: {name}")
            print(f" Author Country: {country}")
    except Exception as e:
        db.rollback()
        raise e


# View all books from database


def view_all_books():
    try:
        # print("View details of all books")
        cursor.execute(''' SELECT
                    book.id,
                    book.title,
                    book.qty,
                    book.authorID,
                    author.name,
                    author.country
                    FROM book
                    INNER JOIN author
                    ON book.authorID = author.id
                    ''')
        books = cursor.fetchall()
        for book in books:
            (id, title, qty, authorID, name, country) = book
            print("\n---------------------------------")
            print(f" Book Title:{title}")
            print(f" Auther Name: {name}")
            print(f" Author Country: {country}")
            print("\n---------------------------------")
    except Exception as e:
        db.rollback()
        raise e


# disply menu untile user select e
try:
    # calling create_table() function to establish database connection and create tables
    db, cursor = connect_db()
    create_table()
    while True:
        print("Please select from the following menu:")
        print("a- Enter Book")
        print("u - Update Book")
        print('del - Delete Book')
        print("s - Search Book")
        print("vb - View detais of all books")
        print("e - exit the menu")
        users_choice = input("Please enter your choice from the Menu:")
        if users_choice == "a":
            enter_book()
        elif users_choice == "u":
            update_book()
        elif users_choice == "del":
            delete_book()
        elif users_choice == "s":
            search_book()
        elif users_choice == "vb":
            view_all_books()
        elif users_choice == "e":
            print("Good Bye!")
            db.close()
            exit()
        else:
            print("Please select valid option from the menu")
except Exception as e:
    raise e
finally:
    db.close()
