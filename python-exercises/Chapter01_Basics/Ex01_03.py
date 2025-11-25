# Flow control (if, elif, else)
# Ex-1: Positive / Negative / Zero
num = int(input("Enter your number: "))
if num > 0:
    print("Number is Positive.")
elif num < 0:
    print("Number is Negative.")
else:
    print("Number is zero.")

# Ex-2: Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is larger.")
elif a == b:
    print("Both the numbers are equal.")
else:
    print("Second number is larger.")

# Ex-3: Check eligibility of voting
age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Ex-4: Scoring of greade based on marks
marks = int(input("Enter your marks: "))
if marks > 90:
    print("Your grade is: A ")
elif marks > 75:
    print("Your grade is: B ")
elif marks > 50:
    print("Your grade is: C ")
else:
    print("Your grade is: Fail ")

# Ex-5: Check divisible by 5 and 11
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")

# Ex-6: Simple password checking (login)
password = input("Enter your password: ")
if password == "admin@123":
    print("Login Successfull.")
else:
    print("Login Fail. Check your password.")


