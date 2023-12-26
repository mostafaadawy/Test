# Python Modules
# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# Use a Module
# Now we can use the module we just created, by using the import statement:
import mymodule
mymodule.greeting("Jonathan")
# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
# Save this code in the file mymodule.py
a = mymodule.person1["age"]
print(a)
# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
# Create an alias for mymodule called mx:
import mymodule as mx

a = mx.person1["age"]
print(a)
# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
# Import and use the platform module:
import platform
x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)
# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
# The module named mymodule has one function and one dictionary:
from mymodule import person1
print (person1["age"])


























































