# With statement
# It is used to wrap the execution of a block with methods defined by a context manager.
# It is used to handle exceptions and ensure that resources are released properly.

# It is used to handle files, database connections, etc.

# File handling without with statement
file = open("test.txt", "w")
file.write("Hello, World!")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

# File handling with with statement
with open("test.txt", "w") as file:
    file.write("Hello, World!")

with open("test.txt", "r") as file:
    print(file.read())

# Supporting with statement in user defined objects
class MyClass:
    def __enter__(self):
        print("Entering the block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the block")

with MyClass() as obj:
    print("Inside the block")
