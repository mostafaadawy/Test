# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

txt = " Hello, World! "
print(len(txt))
if "free" in txt:
  print("Yes, 'free' is present.") #include
print("expensive" not in txt) # not onclude
print(txt[2:5])
print(txt[:5])
print(txt[2:])
print(txt[-5:-2])
print(txt.upper())
print(txt.lower())
print(txt.strip()) # such as trim in java
print(txt.replace("H", "J"))
print(txt.split(",")) # returns ['Hello', ' World!'
age = 36
# txt = "My name is John, I am " + age # return error can not concat string with integer
txt = "My name is John, I am " + str(age) # explict cast to solve
print(txt)
# Other solution to use str,format
txt = "My name is John, I am {} and has {} books" 
print(txt.format(age,300))
# Escape Chars \' \n  ...
txt = 'It\'s alright.'
print(txt) 
txt = "This will insert one \\ (backslash)."
print(txt) 
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\rWorld!"
print(txt) 
txt = "Hello\tWorld!"
print(txt) 
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
# String Methods
# Python String capitalize() and casefold()Method
txt = "hello, and welcome to my world. python is FUN!"
x = txt.capitalize()
print (x)
x = txt.casefold()
print (x)
#  We Can Cascade using methods
x = txt.casefold().capitalize()
print (x)
# Python String center() Method
txt = "banana"
x = txt.center(20)
print(x)
x = txt.center(20, "O")
print(x)
# Python String count() Method
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
# Python String encode() Method
txt = "My name is Ståle"
x = txt.encode()
print(x)
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# Python String endswith() Method
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
x = txt.endswith("my world.")
print(x)
x = txt.endswith("my world.", 5, 11)
print(x)
# Python String expandtabs() Method
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
# Python String find() Method
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
x = txt.find("e")
print(x)
x = txt.find("e", 5, 10)
print(x)
print(txt.find("q"))
print(txt.index("e"))
# Python String find() Method
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1,txt2,txt3)
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))
#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5))
#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5))
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))
#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))

# Python String index() Method
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
x = txt.index("e")
print(x)
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)
txt = "Hello, welcome to my world."
# Python String isalnum() Method Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)
txt = "Company 12"
x = txt.isalnum()
print(x)
# Python String isalpha() Method
txt = "CompanyX"
x = txt.isalpha()
print(x)
txt = "Company10"
x = txt.isalpha()
print(x)
# Python String isascii() Method
txt = "Company123"
x = txt.isascii()
print(x)
# Python String isdecimal() Method
txt = "1234"
x = txt.isdecimal()
print(x)
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())
# Python String isdigit() Method
txt = "50800"
x = txt.isdigit()
print(x)
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())
# Python String isidentifier() Method
txt = "Demo"
x = txt.isidentifier()
print(x)
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
# Python String islower() Method
txt = "hello world!"
x = txt.islower()
print(x)
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())
# Python String isnumeric() Method
txt = "565543"
x = txt.isnumeric()
print(x)
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
# Python String isprintable() Method
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
# Python String isspace() Method
txt = "   "
x = txt.isspace()
print(x)
txt = "   s   "
x = txt.isspace()
print(x)
# Python String istitle() Method
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
# Python String isupper() Method
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())
print(b.isupper())
print(c.isupper())
# Python String join() Method
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
# Python String ljust() Method
# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
x = txt.ljust(20, "O")
print(x)
# Python String lower() Method
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
# Python String lstrip() Method
# Remove spaces to the left of the string:
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
txt = ",,,,,ssaaww.....banana"
# Remove the leading characters:
x = txt.lstrip(",.asw")
print(x)
# Python String maketrans()
# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))
# Python String partition() Method
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)
# Python String replace() Method
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)
# Python String rfind() Method The rfind() method finds the last occurrence of the specified value.
# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)
txt = "Hello, welcome to my world."
print(txt.rfind("w"))
print(txt.rindex("w"))
# Python String rindex() Method
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)
txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)
# Python String rjust() Method
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
txt = "banana"
x = txt.rjust(20, "O")
print(x)
# Python String rpartition() Method
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string. The second element contains the specified string. The third element contains the part after the string
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)
# Python String rsplit() Method
# Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)
# Python String rstrip() Method
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)
# Python String split() Method Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)
# Python String splitlines() Method Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)
# Python String startswith() Method
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)
# Python String strip() Method
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
# Python String swapcase() Method
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
# Python String title() Method
txt = "Welcome to my world"
x = txt.title()
print(x)
txt = "Welcome to my 2nd world"
x = txt.title()
print(x)
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)
# Python String translate() Method The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table. Use the maketrans() method to create a mapping table. If a character is not specified in the dictionary/table, the character will not be replaced. If you use a dictionary, you must use ascii codes instead of characters.
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
# Python String upper() Method
txt = "Hello my friends"
x = txt.upper()
print(x)
# Python String zfill() Method The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length. If the value of the len parameter is less than the length of the string, no filling is done.
txt = "50"
x = txt.zfill(10)
print(x)
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))






















































































