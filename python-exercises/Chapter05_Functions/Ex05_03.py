# Ex05_03.py — Recursion & scope examples (with calls)
# Ex05_03 — Recursive Functions

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
