import requests


def login():
    
    resp = requests.get(
        "https://jsonplaceholder.typicode.com/users/", verify=False)
    users = resp.json()
    users = [{"name": user["name"], "email":user["email"]} for user in users]

    
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    if name == "" or email == "":
        print("invalid input")
        return False
    
    
    for user in users:
        if user["name"] == name and user["email"] == email:
            print("logged in successfully")
            return True
    
    print("invalid input")
    return False
