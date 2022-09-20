import login
from switch_functions import *
from details_for_db import l, start_db


if login.login() == True:
    start_db()

    while True:
        print("What do you want to do?")
        print(
                "For adding a book - Press 1\n",
                "For deleting a book - Press 2\n",
                "For changing books locations - Press 3\n",
                "For registering a new reader - Press 4\n",
                "For removing a reader - Press 5\n",
                "For searching books by author - Press 6\n",
                "For reading a book by a reader - Press 7\n",
                "For ordering all books - Press 8\n",
                "For saving all data - Press 9\n",
                "For loading data - Press 10\n",
                "For exit - Press 11\n")
        choise = int(input("your choice: "))
        match choise:
            case 2: delete_abook(l)
            case 3: change_abook(l)
            case 4: register_anew_reader(l)
            case 5: remove_areader(l)
            case 6: search_abook_by_author(l)
            case 7: read_abook_by_areader(l)
            case 8: order_all_books(l)
            case 9: save_all_data(l)
            case 1: add_abook(l)
            case 10:load_data(l)
            case 11: break
