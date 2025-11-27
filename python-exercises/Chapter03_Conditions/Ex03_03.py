# Ex03_03 — Nested & Logical Conditions
# 1) Login system
username = input("Enter user name: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password!")
else:
    print("Unknown user!")


