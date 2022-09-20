import datetime
import time


class Book:
    def __init__(self, author, title, num_of_pages) -> None:
        self.num_of_pages = num_of_pages
        self.title = title
        self.author = author
    
    def normelize(self):
        obj = {
            "num_of_pages":self.num_of_pages,
            "title":self.title,
            "author": self.author
        }
        return obj
    

class Shelf:
    def __init__(self) -> None:
        self.books = []
        self.is_shelf_full = False

    def add_book(self, book):
        if self.is_shelf_full:
            print("shelf full")

        elif not isinstance(book, Book):
            print("Input Error")

        else:
            self.books.append(book)

            if len(self.books) == 5:
                self.is_shelf_full = True

    def replace_books(self, location1, location2):

        if len(self.books) < location1 or location2:
            print("Empty location")

        elif location1 or location2 < 1:
            print("Index Error")

        elif location1 == location2:
            pass

        else:
            self.books[location1], self.books[location2] =\
                self.books[location2], self.books[location1]

    def order_books(self):
        self.books.sort(key = lambda x: x.num_of_pages)


class Reader:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.books = []

    def read_book(self, title):

        time_stamp = datetime.datetime.fromtimestamp(
            time.time()).strftime('%d/%m/%Y')

        obj = {
            "title": title, 
            "dete": time_stamp
            }

        self.books.append(obj)


class Library:
    def __init__(self) -> None:
        self.shelves = []
        self.readers = []

    def is_there_place_for_new_book(self):

        for shelf in self.shelves:
            if not shelf.is_shelf_full:
                return True
            return False

    def add_new_book(self, book):

        if not isinstance(book, Book):
            print("Error! Invalid data")

        elif not self.is_there_place_for_new_book:
            print("The Library is full")

        elif len(self.shelves) == 0:
            shelf = self.shelves[0]
            shelf.books.append(book)
            print("added book " + book.title)

        else:
            for shelf in self.shelves:
                if not shelf.is_shelf_full:
                    shelf.books.append(book)
                    print("added book " + book.title)

                    if len(shelf.books) == 5:
                        shelf.is_shelf_full = True
                    
                    return

    def delete_book(self, title):
        for shelf in self.shelves:
            for book in shelf.books:

                if book.title == title:
                    shelf.books.remove(book)

                    print("removed")

                    shelf.is_shelf_full = False
                    return
        
        print("book not exist")

    def search(self, title):
        if not isinstance(title, str):
            print("invalid input")
            return

        for i,shelf in enumerate(self.shelves):
            for b in shelf.books:
                if title == b.title:
                    print("find book in index " + str(i) + " , " + str(shelf.books.index(b)))
                    return i, shelf.books.index(b)

        print("book not found")

        return -1, -1

    def change_location(self, title1, title2):

        if not isinstance(title1 and title2, str):

            print("invalid input")
            return

        sh1, b1 = self.search(title1)
        sh2, b2 = self.search(title2)

        if b1 >= 0 and b2 >= 0:
            self.shelves[sh1].books[b1], self.shelves[sh2].books[b2] =\
                self.shelves[sh2].books[b2], self.shelves[sh1].books[b1]

            print("books location changhed")
            return
        
        print("change location fail")

    def change_locations_in_same_shelf(self, shelf_number, location1, location2):

        if not isinstance(shelf_number and location1 and location2, int):
            print("invalid input")
            return

        self.shelves[shelf_number].replace_books(location1, location2)
        
        print("Raplaced successfully")
    
    def order_books2(self):

        list(map(lambda x:x.order_books(), self.shelves))
        print("updated")
    
    def register_reader(self, name, id):

        if not isinstance(name, str) or not isinstance(id, int):
            print("invalid input")
            return
        
        reader = Reader(id, name)

        self.readers.append(reader)

        print("reader registered")
    
    def remove_reader(self, name):

        if not isinstance(name, str):
            print("invalid input")

            return
        list(filter(lambda x: self.readers.remove(x)
             if x.name == name else x, self.readers))
 
    def reader_read_book(self, title, name):

        if not isinstance(title and name, str):
            print("invalid input")
            return
       
        for r in self.readers:
            if r.name == name:
                r.read_book(title)
                print("add the book " + title + " in " + name + "'s book list")
                return
       
        print("add book fail")
    
    def search_by_author(self, author):

        if not isinstance(author, str):
            print("Value Error")
            return

        books = []

        list(map(lambda i: list(filter(lambda j: books.append(j.title)
             if j.author == author else j, i.books)), self.shelves))

        print(author + " write the books: ", books)