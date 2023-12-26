print("----------------NumPy ufuncs-----------------------")
print("-ufuncs stands for 'Universal Functions' and they are NumPy functions that operate on the ndarray object.--")
# Why use ufuncs?
# funcs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
# ufuncs also take additional arguments, like:
# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.
# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.
# It is faster as modern CPUs are optimized for such operations.
# Add the Elements of Two Lists
# list 1: [1, 2, 3, 4]
# list 2: [4, 5, 6, 7]
# One way of doing it is to iterate over both of the lists and then sum each elements.
print("------------------Without ufunc, we can use Python's built-in zip() method--------------------")
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)
print("------------------NumPy has a ufunc for this, called add(x, y) that will produce the same result.--------------------")
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)
print("--------------Create Your Own ufunc-----------------")
# To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
# The frompyfunc() method takes the following arguments:
# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.
def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print("--------------Check if a Function is a ufunc-----------------")
print(type(np.add))
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')
print("--------------Simple Arithmetic-----------------")
# Simple Arithmetic
# You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.
# Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.
# All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
print("--------------Addition-----------------")
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
print("--------------Addition-----------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)
print("--------------Multiplication---ele by ele--------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print(newarr)
print("--------------Division---ele by ele--------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)
print("--------------Power---ele by ele--------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)
print("--------------Mode---ele by ele--------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)
print("--------------Remainder---ele by ele--------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.remainder(arr1, arr2)
print(newarr)
print("--------------Quotient and Mod---ele by ele--------------")
print("---The divmod() function return both the quotient and the the mod.----")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print(newarr)
print("--------------Absolute Values--------------")
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)
print("--------------Rounding Decimals--------------")
# There are primarily five ways of rounding off decimals in NumPy:
# truncation,fix,rounding,floor,ceil
print("--------------Truncation--Fix------------")
print("----Remove the decimals, and return the float number closest to zero----")
arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr = np.fix([-3.1666, 3.6667])
print(arr)
print("--------------Rounding------------")
arr = np.around(3.1666, 2)
print(arr)
print("--------------Floor------------")
arr = np.floor([-3.1666, 3.6667])
print(arr)
print("--------------Ceil------------")
arr = np.ceil([-3.1666, 3.6667])
print(arr)
print("--------------NumPy Logs------------")
print("---NumPy provides functions to perform log at the base 2, e and 10----")
print("--------------Log at Base 2------------")
arr = np.arange(1, 10)
print(np.log2(arr))
# Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
print("--------------Log at Base 10------------")
arr = np.arange(1, 10)
print(np.log10(arr))
print("--------------Natural Log, or Log at Base e------------")
arr = np.arange(1, 10)
print(np.log(arr))
# print("--------------Log at Any Base------------")
# nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15))
print("--------------array summsion nod adding tow array------------")
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)
print("-----------Summation Over an Axis---------")
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
print("-----------Cummulative Sum---cumsum()------")
print("---Cummulative sum means partially adding the elements in array.---")
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)
print("-----Prod()------NumPy Products all arr elements multiplicatio by each other------")
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)
print("-----------Product Over an Axis---------")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
print("-----------Cummulative Product---------")
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)
print("----diff()-------NumPy Differences---------")
# A discrete difference means subtracting two successive elements.
# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
# We can perform this operation repeatedly by giving parameter n.
# E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
print("--------NumPy LCM Lowest Common Multiple-----------")
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
print("--------Finding LCM in Arrays-----------")
# To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
# The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)
print("--------NumPy GCD Greatest Common Denominator-----------")
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
print("--------Finding GCD in Arrays-----------")
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
print("--------NumPy Trigonometric Functions-----------")
# NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
print("--------sin-----------")
x = np.sin(np.pi/2)
print(x)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)
print("--------Convert Degrees Into Radians----------")
# By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
print("--------Convert Radians to Degreess----------")
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)
print("--------Finding Angles----------")
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
# NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
x = np.arcsin(1.0)
print(x)
print("--------Angles of Each Value in Arrays----------")
x = np.arcsin(arr)
print(x)
print("--------Hypotenues----------")
# Finding hypotenues using pythagoras theorem in NumPy.
# NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
print("--------NumPy Hyperbolic Functions----------")
# NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
x = np.sinh(np.pi/2)
print(x)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)
print("--------Finding Angles----------")
# Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
# Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.
x = np.arcsinh(1.0)
print(x)
print("--------Angles of Each Value in Arrays----------")
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
print("--------NumPy Set Operations----------")
# What is a Set
# A set in mathematics is a collection of unique elements.
# Sets are used for operations involving frequent intersection, union and difference operations.
# Create Sets in NumPy
# We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.
print("--------Create Sets in NumPy----------")
print("--------Convert following array with repeated elements to a set----------")
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
print("--------Finding Union----------")
# To find the unique values of two arrays, use the union1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
print("--------Finding Intersection----------")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
# Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
print("--------Finding Difference----------")
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
# Note: the setdiff1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
print("--------Finding Symmetric Difference----------")
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)
# Note: the setxor1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
