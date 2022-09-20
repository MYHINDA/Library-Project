import json

from Library import Book
from details_for_db import client


def add_abook(lib):
    
    title = input("Enter The Book Title: ")
    author = input("Enter the author: ")
    num_of_pages = input("Enter number of pages in the book: ")
    book = Book(author,title,num_of_pages)
    lib.add_new_book( book)
    
def delete_abook(lib):
    title = input("Enter the title of book you want to delete")
    lib.delete_book(title)
    
def change_abook(lib):
    title1 = input("enter the title of the first book to change")
    title2 = input("enter the second title")
    lib.change_location(title1, title2)
    
def register_anew_reader(lib):
    name = input("Enter the reader name: ")
    id = int(input("Enter the reader id: "))
    lib.register_reader(name, id)
    
def remove_areader(lib):
    name = input("Enter name of reader to remove: ")
    lib.remove_reader(name)
    print("Removed reader " + name + " from list")

def search_abook_by_author(lib):
    author = input("Enter an author name: ")
    lib.search_by_author(author)

def read_abook_by_areader(lib):
    
    id = int(input("Enter the reader's id: "))

    if list(filter(lambda x: x.id == id, lib.readers)) == []:
        print("reader not exist")
        return

    title = input("Enter the title of the book: ")

    def temp(rdr):
        rdr.read_book(title)
        lib.reader_read_book(title, rdr.name)
        
    list(filter(lambda rdr: temp(rdr) if rdr.id ==
         id else rdr, lib.readers))

def order_all_books(lib):
    lib.order_books2()

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
