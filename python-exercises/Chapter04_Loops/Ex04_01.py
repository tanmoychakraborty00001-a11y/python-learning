# Ex04_01 — For Loops
# 1) Print 1 to 10
# Applying range function
for i in range(1, 11):
    print(i)

# 2) Sum of first 10 numbers
s = 0
for i in range(1, 11):
    s += i
print("Sum is: ", s)

# 3) Print even numbers 1–20
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 4) Print characters of a string
name = "PYTHON"
for ch in name:
    print(ch)

# 5) Multiplication table
num = int(input("Enter any number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)