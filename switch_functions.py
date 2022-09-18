from Library import Book, Reader, Library
from details_for_db import client
import json


def add_abook():
    book = Book()
    book.title = input("Enter The Book Title: ")
    book.author = input("Enter the author: ")
    book.num_of_pages = input("Enter number of pages in the book: ")
    Library.add_new_book(book)
    

def delete_abook():
    title = input("Enter the title of book you want to delete")
    Library.delete_book(title)
    

def change_abook():
    title1 = input("enter the title of the first book to change")
    title2 = input("enter the second title")
    Library.change_location(title1, title2)
    

def register_anew_reader():
    name = input("Enter the reader name: ")
    id = int(input("Enter the reader id: "))
    Library.register_reader(name, id)
    

def remove_areader():
    name = input("Enter name of reader to remove: ")
    Library.remove_reader(name)
    print("Removed reader " + name + " from list")


def search_abook_by_author():
    author = input("Enter an author name: ")
    Library.search_by_author(author)


# take name or id??
def read_abook_by_areader():
    name = input("Enter the reader's name: ")
    title = input("Enter the title of the book: ")
    Reader.read_book(title)
    Library.reader_read_book(title,name)


def order_all_books():
    Library.order_books2()


def save_all_data():

        
    library = client.get_database('Library')

    shelves = library.get_collection('Library').find()

    shelves = [{"is_shelf_full": shelf["is_shelf_full"],
                "books:": shelf["books"]} for shelf in shelves]

    db = client.get_database('Readers')

    readers = db.get_collection('Readers').find()
    readers = [{"id": reader["id"], "name": reader["name"],
                "books": reader["books"]} for reader in readers]

    file_name = input("Enter file name: ")
    file_name = './' + file_name + '.json'

    with open(file_name, 'w', encoding='utf_8') as file:

        file.write("{ \"shelves:\": ")
        file.write(json.dumps(shelves, indent=2))

        file.write(",")
        file.write("\"readers:\":")
        file.write(json.dumps(readers, indent=2))

        file.write("}")




def load_data():
    db = client["New_data"]

    collection = db["New_data"]
    file_name = input("Enter file data name: ")
    with open("./" + file_name + ".json", 'r') as f:

        my_data = json.load(f)
        if isinstance(my_data, list):
            collection.insert_many(my_data)
        else:
            collection.insert_one(my_data)




