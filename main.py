"""
Arrays and array-like structures are fundamental to programming and computer
science. Most of the programming you will do will work with array-like
structures so it is critical to understand them and the differences between
them. This set of examples will walk you through the different array-like
structures in Python, but all languages have similar concepts. The most
important thing to note is that all array-like structures basically work
the same. It's all about the index or key that you use to access the structure.
Once you understand the index or key structure and how the hierarchy of indexes
and keys work, then all array-like structures work the same.
"""

# bring numpy arrays into Python (they are not part of Python natively)
import numpy as np

# for use in the examples to make random numbers
import random

# constants to control the examples. you can change these to whatever you
# like and the examples still work. make sure you understand this and why.
SIZE = 5
ROWS = 3
COLS = 4

######################################
# NUMPY ARRAY EXAMPLES
######################################

# this creates a numpy array. it has the characteristics that
# it is a fixed size of SIZE and fixed type, in this case ints.
numbers = np.array([0] * SIZE, dtype=int)

# put the number 6 in the second position
numbers[1] = 6

# read the number from the second position
print(numbers[1])

# put the number 10 in all positions
for i in range(SIZE):
    numbers[i] = 10

# print all the numbers in the array, one per line, along with the index
for i in range(SIZE):
    print(i, ":", numbers[i])

# OR just dump out the whole array all at once.
print(numbers)
print()

######################################
# PYTHON LIST EXAMPLE
######################################

"""
A python list is an array-like structure. Technically it is not an array.
It is an object with array-like properties and you use it like an array,
and you can do many other things with it. The basics of array usage still apply.
"""

# Python lists are variable size and variable type
# contrast that with numpy arrays which are fixed/fixed.

# this makes an list with three elements of differnt types; int, string, float
python_list = [10, "cat", 3.14]

# print all the values in the list, one per line, along with the index
s = len(python_list) # first get the size of the list
for i in range(s):
    print(i, ":", python_list[i])

# you can add items to the list dynamically
python_list.append("dog")

#print the last item in the list
print(python_list[-1])

# you can dump out the whole list all at once.
print(python_list)
print()

######################################
# PYTHON TUPLE EXAMPLES
######################################
"""
A Python Tuple is an array like structure that is exactly the same as a list
except you cannot dynamically alter the size. So a tuple is a list that is
fixed size with variable types.
"""

# make a tuple of various types
python_tuple = (100, "hello", 3.14, "world")

# print all the values in the tuple, one per line, along with the index
s = len(python_tuple) # first get the size of the tuple
for i in range(s):
    print(i, ":", python_tuple[i])

# OR just dump out the whole tuple all at once.
print(python_tuple)
print()

######################################
# PYTHON DICTIONARY EXAMPLES
######################################
"""
A Python Dictionary is an array like structure that is exactly the same as a
list except the indexes are not numbers, they are keys (a string).
So a dictionary is a list that is variable size with variable types and has
a key instead of an index.
"""

# create a dictionary of key:value pairs
python_dictionary = {"one": 50, "pi": 3.14, "helloworld": "this is a longer string"}

for key in python_dictionary:
    print(key, ":", python_dictionary[key])

# OR just dump out the whole tuple all at once.
print(python_dictionary)

# you can also access the keys only and extract them
print(python_dictionary.keys()) # this will give you dict_keys object

# you can put keys into a list to use them later
keys = list(python_dictionary.keys())
print(keys)

# by doing that, you can also use keys dynamically and access
# the dictionary with numeric indexes
print(python_dictionary[keys[0]])

# you can add items to the dictionary dynamically
# just make a new key with a new value
python_dictionary["dog"] = "cat"

#print the item just added
print(python_dictionary["dog"])

# you can dump out the whole list all at once.
print(python_dictionary)
print()

######################################
# Array-like structures inside array-like structures.
# i.e. multidimensional arrays.
######################################

"""
You can place any array like structure inside another array like structure.
This creates what is known as a multimentional array.
"""
# create a ROWS x COLS array
num2d = np.zeros((ROWS, COLS), dtype=int)

# show the array
print(num2d)

# fill the array with numbers
# 1,1,1,1
# 2,2,2,2
# 3,3,3,3
for i in range(ROWS):
    for j in range(COLS):
        num2d[i][j] = i+1
        
# show the array
print(num2d)

# print each row one at at a time
for i in range(ROWS):
    print(num2d[i])
    
# print each element one at a time
for i in range(ROWS):
    for j in range(COLS):
        print(num2d[i][j], end=" ")
    print()
print()


# it is VERY common to make n-dimension "arrays" with dictionaries
# the following is a 2D dictionary where the "rows" are accessed by each key
# and the "columns" are each piece of data in the lists in the dictionary.
# i.e. this is a 1D dictionary that holds multiple 1D lists

# make a dictionary that holds three people's names as keys
# and has their age, gender, and favorite color as each value
people = {"alice": [29, "f", "red"], "bob": [24, "m", "green"], "charlie": [32, "m", "blue"]}

# show the dictionary
print(people)

# add 1 to everyone's age
for name in people:
    # this goes to the 1st element in the list accessed by the name
    people[name][0] += 1

# show the dictionary
print(people)

# flip everyone's gender
for name in people:
    if people[name][1] == 'm':
        people[name][1] = 'f'
    else:
        people[name][1] = 'm'
        
# show the dictionary
print(people)

# capitalize all the colors
for name in people:
    people[name][2] = people[name][2].upper()
        
# show the dictionary
print(people)

# change bob's color to purple
people['bob'][2] = 'purple'

# show the dictionary
print(people)
print()

######################################
# Strings
######################################

"""
Strings are also an array-like structure in all languages.
In Python they are tuples with a fixed type; characters.
i.e. A string in Python is a fixed size fixed type list
that contains only character types.
"""

# make a string
mystring = "hello world"

# print each character one at a time
for ch in mystring:
    print(ch, end="")
print()

# print each character one at a time using indexes
l = len(mystring)
for i in range(l):
    print(mystring[i], end="")
print()

# capitalize every other letter into a new string
new_string = ""
for i in range(l):
    if i%2:
        new_string += mystring[i].upper()
    else:
        new_string += mystring[i]

print(new_string)

# print the string backwards
for i in range(l-1, -1, -1):
    print(mystring[i], end="")
print()
print()

########################################################
# USING FLAGS TO CONTROL FUNCTIONS
########################################################

# create an 'empty' numpy array of size SIZE
rnums = np.empty(SIZE, dtype="int")

# fill the array with randome integers from 1 to 10 (inclusive)
for i in range(SIZE):
    rnums[i] = random.randint(1,10)

#show the array
print(rnums)

#create a function that will optionally send back a total of an np array or an average
def sum_avg1(arr, avg):
    answer = 0
    for n in arr:
        answer += n
    if(avg):
        answer = float(answer) / float(len(arr))
    return answer

# show the usage of the function
print("This is the total: ", sum_avg1(rnums, False))
print("This is the average: ", sum_avg1(rnums, True))

#create similar function with with a default value
def sum_avg2(arr, avg=False):
    answer = 0
    for n in arr:
        answer += n
    if(avg):
        answer = float(answer) / float(len(arr))
    return answer

# show the usage of the function
print("This is the total: ", sum_avg2(rnums))
print("This is the average: ", sum_avg2(rnums, True))

########################################################
# PROFESSIONAL CODING
########################################################
"""
In the fucntions above there is no error checking for passed in values.
This would not be acceptable in ANY professional code. It is ALWAYS
your responsibility to check for errors in data and data types.
The following demonstrates a complete, professional version of sum_avg.
This will also demonstrate the correct usage of the Try/Except statement.
"""

#create similar function with with a default value
def sum_avg3(arr, avg=False):

    answer = 0
    if type(arr) != type(np.empty(0, dtype="int")):
        raise TypeError('array must be a Numpy integer array')
    elif type(avg) != bool:
        raise TypeError('parameter min must be Boolean')
    else:
        for n in arr:
            answer += n
        if(avg):
            answer = float(answer) / float(len(arr))
    return answer

# show the usage of the function
try:
    print("This is the total: ", sum_avg3(rnums))
except TypeError as e:
    print(e)

# now try it with a non-numpy array
a = [10,20,30] # this is a Python List, not a Numpy array
try:
    print("This is the total: ", sum_avg3(a))
except TypeError as e:
    print(e)

# now try it with a float instead of a boolean for min
n = 1.234
try:
    print("This is the average: ", sum_avg3(rnums, n))
except TypeError as e:
    print(e)

print()



