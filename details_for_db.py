from Library import Book, Shelf, Reader, Library
from pymongo import MongoClient
import requests


client = MongoClient(port=27017)
l = Library()


def start_db():

    db_name = "LIBRARY"
    db = client[db_name]

    collection_users = "Users"
    collection_library = "Library"
    collection_readers = "Readers"

    list_names = db.list_collection_names()

    if collection_users in list_names:
        db.drop_collection(collection_users)
    db.create_collection(collection_users)

    user_documents = db[collection_users]

    resp = requests.get(
        "https://jsonplaceholder.typicode.com/users", verify=False)

    users = resp.json()

    for user in users:
        user_documents.insert_one(user)


    if collection_library in list_names:
        db.drop_collection(collection_library)

    db.create_collection(collection_library)

    library_documents = db[collection_library]

    b = Book("Hinda", "a", 100)
    b1 = Book("Avi", "b", 150)
    b2 = Book("Dana", "c", 120)
    b3 = Book("Sara", "d", 15)
    b4 = Book("Rami", "e", 10)
    b5 = Book("mi", "f", 1000)

    s1 = Shelf()
    s2 = Shelf()
    s3 = Shelf()

    l.shelves.append(s1)
    l.shelves.append(s2)
    l.shelves.append(s3)

    s1.add_book(b)
    s1.add_book(b1)
    s2.add_book(b3)
    s2.add_book(b2)
    s3.add_book(b5)
    s3.add_book(b4)

    for shelf in l.shelves:
        books = [x.normelize() for x in shelf.books]
        obj = {"is_shelf_full": shelf.is_shelf_full, "books": books}
        library_documents.insert_one(obj)


    if collection_readers in list_names:
        db.drop_collection(collection_readers)

    db.create_collection(collection_readers)

    reader_documents = db[collection_readers]

    r1 = Reader(1, "Hinda")
    r2 = Reader(2, "Hershtik")

    r1.read_book("AA")
    r2.read_book("BB")

    l.readers.append(r1)
    l.readers.append(r2)

    for reader in l.readers:
        obj = {"id": reader.id, "name": reader.name, "books": reader.books}
        reader_documents.insert_one(obj)
