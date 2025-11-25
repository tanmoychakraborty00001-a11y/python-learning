# Program 1: Hello World
print("Hellow World!")

# Program 2: Addition
a = 10
b = 20
print("Sum is: ", a + b)

# Basic string formatting
name = "Tanmoy"
msg = "Hello, {}!".format(name)
print(msg)

# Integer formatting
age = 25
text = "Your age is {}".format(age)
print(text)

# Multi Integer formatting
a = 10
b = 20
text_int = "a = {}, b = {}".format(a, b)

# Multiple data types (string, int, float) formatting
name = "laptop"
price = 49950
rating = 4.7
msg = "{}costs Rs.{} and has rating {}".format(name, price, rating)
print(msg)

# Formatting specific order
text = "Second: {1}, First: {0}".format("A", "B")
print(text)

# Formatting integers with width
num = 7
text = "Number: {:03d}".format(num)
print(text)

# Formatting with decimal places(floats)
pi = 3.14159
text = "Pi = {:.2f}".format(pi)
print(text)

# Formatting with named arguments
msg = "My name is {n} and I am {a} years old".format(n = "Tanmoy", a = 30)
print(msg)