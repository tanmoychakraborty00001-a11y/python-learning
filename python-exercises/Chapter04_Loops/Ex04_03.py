# Ex04_03 — Pattern Printing
# 1) Square of stars
for i in range(5):
    print("*" * 5)

# 2) Increasing triangle
for i in range(1, 6):
    print("*" * i)

# 3) Decreasing triangle
for i in range(5, 0, -1):
    print("*" * i)

# 4) Number triangle
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = "")
    print()

# 5) Reverse number triangle
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end = "")
    print()