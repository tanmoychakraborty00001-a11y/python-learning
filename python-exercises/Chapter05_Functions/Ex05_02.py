# Ex05_02 — Default Arguments, Variable Arguments, Scope

# 1) Function with default arguments
# Function power(base, exponent=2) → square if exponent not given.

def power(base, exponent=2):
    return(base ** exponent)
print(power(3))

# 2) Sum of all numbers using *args
# Function sum_all(*nums) → return total of all arguments.

def sum_all(*nums):
    return(sum(nums))
print(sum_all(5, 4, 3, 2, 1))

# 3) Print student info using **kwargs (keywords arguments)
# Function student_info(**data) → print key=value pairs.

def student_info(**data):
    return(data)
print(student_info(name = "Tanmoy", age = 30, grade = "A", city = "Mumbai"))

def greet_user(name, age=18, *hobbies):
    return{"name": name, "age": age, "Hobbies": hobbies}
print(greet_user("Amit", 25, "guiter", "Chess"))

# 4) variable scope 
# It defines the region within a program where a variable is accessible and recognized. Python follows the LEGB rule for name resolution, which stands for Local, Enclosing, Global, and Built-in. 

x = 10 # global variable
def modify_local(x):
    x = 50 # local variable; does NOT change global x
    return(x)

print(f"The Glocal variable is: {x}.")
print("The local variable is: ", modify_local(x))

# 5) Modifying the variable

x = 10 # This is global variable
def modify_global():
    global x # modifies global x
    x = 99
    return x
print(modify_global())
    