# Python Scope
# A variable is only available from inside the region it is created. This is called scope.
# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = 300
  print(x)
myfunc()
# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)
# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
















































































