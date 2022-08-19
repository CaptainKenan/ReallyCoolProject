import json

users = []


def get_users():
    try:
        with open("users.txt", "r") as file:
            for line in file:
                users.append(json.loads(line))
            file.close()
    except FileNotFoundError:
        print("File not found!")


def add_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")
    user = {"name": name, "surname": surname, "age": age,}
    users.append(user)


def redact_user():
    opt1 = input("Enter\n1) For Change Name\n2) For Change Surname\n3) For Change Age\nChoose: ")
    if opt1 == "1":
        name1 = input("enter username for replace: ")
        name2 = input("enter new username: ")
        for i in users:
            if i['name'] == name1:
                i['name'] = name2
    elif opt1 == "2":
        surname1 = input("enter surname for replace: ")
        surname2 = input("enter new surname: ")
        for i in users:
            if i["surname"] == surname1:
                i["surname"] = surname2

    elif opt1 == "3":
        age1 = input("enter age for replace: ")
        age2 = input("enter new age: ")
        for i in users:
            if i["age"] == age1:
                i["age"] = age2


def delete_user():
    username = input("Enter username for delete: ")
    for i in users:
        if i['name'] == username:
            users.remove(i)


def search_user():
    surname1 = input("Enter Surname: ")
    for i in users:
        if surname1 in i["surname"]:
            print(i['name'], i["surname"])


def age_show_user():
    op = input("Enter\n1) for show users by age\n2) for show users by surname\nChoose: ")
    if op == "1":
        age1 = input("Enter Age: ")
        for i in users:
            if age1 == i["age"]:
                print(i)
    elif op == "2":
        surnameusers = input("Enter Users Surname: ")
        for j in users:
            if surnameusers == j["surname"]:
                print(j)


def save_users():
    try:
        with open("users.txt", "w") as file:
            for user in users:
                file.write(json.dumps(user) + '\n')
            file.close()
    except FileNotFoundError:
        print("File not found!")


get_users()
while True:
    opt = int(input(
        "1) Show users\n2) Add user\n3) Redact User Name\n4) Delete User by Name\n5) For Search\n6)Show All Information About Users\n7) Exit\nChoose: "))
    if opt == 1:
        for user in users:
            print(f"Name: {user['name']}\nSurname {user['surname']}\nAge: {user['age']}")
    elif opt == 2:
        add_user()
        print("User added!")
    elif opt == 3:
        redact_user()

    elif opt == 4:
        delete_user()
        print("User is deleted")

    elif opt == 5:
        search_user()

    elif opt == 6:
        age_show_user()

    elif opt == 7:
        break
    else:
        print("Wrong option!")
save_users()
