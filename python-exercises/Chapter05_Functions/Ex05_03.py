# Ex05_03.py — Recursion & scope examples (with calls)
# 1) Ex05_03 — Recursive Functions

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# 2) Recursive - Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

# 3)

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)
print(sum_n(5))

# 4) counts digits
def count_digits(n):
    n = abs(n) # handle negative numbers
    if n < 10:
        return 1
    return 1 + count_digits(n//10)
print(count_digits(345))

# 5) reversing string
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))

# 6) palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("racecar"))
