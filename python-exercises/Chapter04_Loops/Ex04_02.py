# Ex04_02 — While Loops, break and continue
# 1) Print numbers 1–5
i = 1
while i <= 5:
    print(i)
    i += 1

# 2) Countdown
n = 5
while n > 0:
    print(n)
    n -= 1

# 3) Stop loop when number is 7
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

# 4) Skip even numbers
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# 5) Sum until user enters 0
sum = 0
while True:
    x = int(input("Enter a number (0 for stopping): "))
    if x == 0:
        break
    sum += x
print("Total: ", sum)