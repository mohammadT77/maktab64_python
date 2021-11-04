from models import User
from exceptions import *


def register_menu():
    print("RegisterMenu")
    print("Enter your profile below:")

    id = input(">> id:")
    username = input(">> username:")
    name = input(">> name:")
    phone = input('>> phone:')
    password = input('>> password:')
    email = input('>> email(opt):')

    try:
        user = User(int(id), username, name, phone, password, email)
        file = user.save()
        print(f"User Registered (file: {file})")
    except UserError as e:
        print("Error:", e, "\nTry again!!!\n")
        register_menu()


def login_menu():
    print("LoginMenu")
    print("Enter your username & password:")

    username = input(">> username:")
    password = input('>> password:')

    try:
        user = User.login(username, password)
        print("Welcome: ", user)
    except LoginError as e:
        print("Error:", e)
        login_menu()


def main_menu():
    print("UserManager")
    print(">> 1. Login")
    print(">> 2. Register")

    opt = input("Enter your option: ")
    if opt == '1':
        login_menu()
    elif opt == '2':
        register_menu()
    else:
        print("Invalid option\n")
        main_menu()
