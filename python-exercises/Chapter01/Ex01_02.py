# Ex-1: Input function asking user input
name = input("Enter your name: ")
print("Hello, ", name)

#Ex-2: Adding two numbers taking inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum of numbers is: ", a + b)

# Ex-3: Age after 10 years
age = int(input("Enter your present age: "))
print("After 10 years you will be: ", age + 10)

# Ex-4: Conversion of temperature Celcius to Farenheit
c = float(input("Enter teperature in Celcius: "))
f = (c * 9/5) + 32
print("Temperature in farenheit: ", f)

# Ex-5: Circle area
r = float(input("Enter the radius: "))
area = 3.14159 * r * r
print("Area of the circle: ", area)

# Ex-6: Simple Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time period: "))
si = (p * r * t) / 100
print("Simple interest is: ", si)

# Ex-7: Checking odd or even taking input of a number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Input number is Even")
else:
    print("Input number is Odd")
