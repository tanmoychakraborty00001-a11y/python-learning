#Folder: Chapter05_Functions

#defining functions

#parameters, return

#default arguments

#variable arguments

#scope

#recursive functions

# Ex05_01 — Basic Functions, Parameters & Return

# 1) Greet user
# Write a function greet(name) that prints "Hello, <name>!".

def greet(name):
    print(f"Hello, {name}!")
greet("Tanmoy")

# 2) Add two numbers
# Function add(a, b) → return the sum.
def add(a, b):
    return a + b
print(add(3, 5))

# 3) Area of a rectangle
# Function area_rectangle(length, breadth) → return area.
def area_rec(l, b):
    return(l * b)
print(area_rec(5, 3))

# 4) Check even/odd
# Function is_even(num) → return True/False.
def is_even(num):
    return num % 2 == 0
print(is_even(4))

# 5) Convert Celsius to Fahrenheit
def cel_to_fer(c):
    return(c * 9/5) + 32
print(cel_to_fer(25))

