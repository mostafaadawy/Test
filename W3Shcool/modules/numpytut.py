print("-----------------------NumPy Tutorial-------------------------")
# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".
# Learning by Reading We have created 43 tutorial pages for you to learn more about NumPy.
# Starting with a basic introduction and ends up with creating and plotting random data sets, and working with NumPy functions:

# What is NumPy?
# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
# NumPy stands for Numerical Python.
# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.

# Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# This behavior is called locality of reference in computer science.
# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.
# Where is the NumPy Codebase?
# The source code for NumPy is located at this github repository https://github.com/numpy/numpy

# NumPy Getting Started
# pip install numpy

# import numpy
# arr = numpy.array([1, 2, 3, 4, 5])
# print(arr)

print("-----------------------Create a NumPy ndarray Object-------------------------")
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(np.__version__)
print(type(arr))

print("----------------------0-D arrays--------------------------")
# Dimensions in Arrays A dimension in arrays is one level of array depth (nested arrays). nested array: are arrays that have arrays as their elements.
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array
arr = np.array(42)
print(arr)

print("----------------------1-D arrays--------------------------")
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array. These are the most common and basic arrays.
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print("----------------------2-D arrays--------------------------")
# 2-D Arrays An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

print("----------------------3-D arrays--------------------------")
# 3-D arrays An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("----------------------Higher Dimentional Arrays--------------------------")
# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
print("----------------------Access Array Elements--------------------------")
# Access Array Elements
print(arr[0])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
# Negative Indexing Use negative indexing to access an array from the end.
print('Last element from 2nd dim: ', arr[1, -1])
print("----------------------Slicing arrays --------------------------")
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step]
# If we don't pass start its considered 0 If we don't pass end its considered length of array in that dimension If we don't pass step its considered 1
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[-3:-1])
print("----------------------Steps--------------------------")
# STEP
print(arr[1:5:2])
# step 2 and Return every other element from the entire array:
print(arr[::2])
print("----------------------Slicing 2-D Arrays--------------------------")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
# From both elements, return index 2:
print(arr[0:2, 2])
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4])

print("------------------------NumPy Data Types------------------------")
# Data Types in Python
# By default Python have these data types:
# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
# Below is a list of all data types in NumPy and the characters used to represent them.
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

print("------------------------Checking the Data------------------------") 
print(arr.dtype)

# Get the data type of an array containing strings
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
print("------------------------Creating Arrays With a Defined Data type------------------------") 
# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
# For i, u, f, S and U we can define size as well. Create an array with data type 4 bytes integer: 
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.
# arr = np.array(['a', '2', '3'], dtype='i')
print("-------------------Converting Data Type on Existing Arrays--------------------")
# Converting Data Type on Existing Arrays
# he best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print("--------------------NumPy Array Copy vs View--------------------")
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

print("--------------------Make a view, change the view, and display both arrays--------------------")
# Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

print("--------------------Check if Array Owns its Data--------------------")
# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

print("----------------------NumPy Array Shape----------------------")
# NumPy Array Shape he shape of an array is the number of elements in each dimension.
print("----------------------Get the Shape of an Array----------------------")
# Get the Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

print("----------------------Create an array with 5 dimensions using ndmin----------------------")
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# Reshaping arrays Reshaping means changing the shape of an array.
print("----------------------Reshape From 1-D to 2-D----------------------")
# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print("----------------------Reshape From 1-D to 3-D----------------------")
# Reshape From 1-D to 3-D
newarr = arr.reshape(2, 3, 2)
print(newarr)
print("----------------------Reshape Into any Shape----------------------")
# Can We Reshape Into any Shape? Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
# Returns Copy or View? Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
# Unknown Dimension You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
# Note: We can not pass -1 to more than one dimension.
# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

print("----------------------Iterating Arrays----------------------")
# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one

print("----------------------Iterating Arrays 1-D ----------------------")
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
for x in arr:
  for y in x:
    print(y)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
for x in arr:
  for y in x:
    for z in y:
      print(z)
print("----------------------Iterating Arrays nditer(arr) ----------------------")
# Iterating on Each Scalar Element In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print('iter',x)

print("-------------------Iterating Array With Different Data Types----------------------")
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
print("-------------------Iterating With Different Step Size----------------------")
# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)
print("-------------------Enumerated Iteration Using ndenumerate()----------------------")
# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
# Enumerate on following 2D array's elements:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print("------------------NumPy Joining Array---------------------")
print("------------------NumPy Joining Array Concat---------------------")
# Joining means putting contents of two or more arrays in a single array.
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

print("------------------NumPy Joining Array Stack---------------------")
# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

print("----------------Stacking Along Rows------------------")
# NumPy provides a helper function: hstack() to stack along rows.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)
print("-----------------Stacking Along Columns-----------------")
# NumPy provides a helper function: vstack()  to stack along columns.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)
print("-----------------Stacking Along Height (depth)-----------------")
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)
print("-----------------Splitting NumPy Arrays-----------------")
# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print("-------------------------------------------------")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
print("------------Split Into Arrays----------------------")
# The return value of the array_split() method is an array containing each of the split as an array.
# If you split an array into 3 arrays, you can access them from the result just like any array element:
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print("------------Splitting 2-D Arrays----------------------")
# Use the same syntax when splitting 2-D arrays.
# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print("------------Split the 2-D array into three 2-D arrays.----------------------")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)
print("------------Split the 2-D array into three 2-D arrays along rows----------------------")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
print("------------An alternate solution is using hsplit() opposite of hstack()----------------------")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
print("------------NumPy Searching Arrays----------------------")
print("------------use the where() method----------------------")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
# The example above will return a tuple: (array([3, 5, 6],) Which means that the value 4 is present at index 3, 5, and 6.
print("------------Find the indexes where the values are even:----------------------")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
print("------------Search Sorted:----------------------")
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
# Example explained: The number 7 should be inserted on index 1 to remain the sort order.
# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
print("------------Search From the Right Side----------------------")
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
print("------------Find the indexes where the values 2, 4, and 6 should be inserted:----------------------")
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
print("------------NumPy Sorting Arrays----------------------")
# Sorting means putting elements in an ordered sequence.
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.
arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) 
# Note: This method returns a copy of the array, leaving the original array unchanged.
print("------------Sort the array alphabetically:----------------------")
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
print("------------Sort a boolean array:----------------------")
arr = np.array([True, False, True])
print(np.sort(arr))
print("------------Sorting a 2-D Array----------------------")
# If you use the sort() method on a 2-D array, both arrays will be sorted:
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
print("------------NumPy Filter Array----------------------")
# Getting some elements out of an existing array and creating a new array out of them is called filtering. In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
print("------------Creating the Filter Array----------------------")
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print("------------Creating Filter Directly From Array----------------------")
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print("------------Creating Filter Directly ُرثى آعةلاثقس----------------------")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

















