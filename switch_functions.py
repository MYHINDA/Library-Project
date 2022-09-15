from Library import Book, Reader, Library


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


def save_all_data(self):
    
    shelves = self.shelves
    # readers = Library.readers
    file_name = input("Enter file name: ")
    file_name = './' + file_name + '.json'
    with open(file_name, 'w', encoding='utf_8' ) as file:
        file.write(shelves)



def load_data():
    pass


