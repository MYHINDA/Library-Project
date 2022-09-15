import details_for_db
import switch_functions

if details_for_db.login() == True:
        
    while True:
        print("What do you want to do?")
        print(
            "For adding a book - Press 1",
            "For deleting a book - Press 2",
            "For changing books locations - Press 3",
            "For registering a new reader - Press 4",
            "For removing a reader - Press 5",
            "For searching books by author - Press 6",
            "For reading a book by a reader - Press 7",
            "For ordering all books - Press 8",
            "For saving all data - Press 9",
            "For loading data - Press 10",
            "For exit - Press 11")
        choise = int(input())
        match choise:
            case 1: switch_functions.add_abook()
            case 2: switch_functions.delete_abook()
            case 3: switch_functions.change_abook()
            case 4: switch_functions.register_anew_reader()
            case 5: switch_functions.remove_areader()
            case 6: switch_functions.search_abook_by_author()
            case 7: switch_functions.read_abook_by_areader()
            case 8: switch_functions.order_all_books()
            case 9: switch_functions.save_all_data()
            case 10:switch_functions.load_data()
            case 11:break
            