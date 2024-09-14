# Decorators

# Decorators are functions that modify the behavior of other functions.
# They are used to add functionality to functions dynamically.
# They are used to wrap the execution of a function with additional code.
# They are used to extend the behavior of functions without modifying their source code.

# Usage of decorators
# 1. Logging
# 2. Timing
# 3. Authentication
# 4. Input validation
# 5. Caching

# Example

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# Decorators with arguments

def pretty_sum(func):
    def wrapper(a, b):
        print("Sum of two numbers is: ", func(a, b))
    return wrapper

@pretty_sum
def sum(a, b):
    return a + b

sum(1, 2)

# Multiple decorators
def decor1(func):
    def wrapper():
        print("Decor1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decor2")
        func()
    return wrapper

@decor1
@decor2
def say_whee():
    print("Whee!")

say_whee()