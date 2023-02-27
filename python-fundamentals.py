'''
Facts
- interpreted language
- dynamically typed
- everything is an object
- syntax relies on whitespace

'''


''' ------------------ Built-in Data Types ------------------ '''
# integer
# float
# complex
# boolean
# special None datatype (similar to null in java/c++)


print(''' ------------------ Sequences ------------------ ''')
# an ordered collection of values
# are iterables
# string, list, tuple, range

# operations for all sequences
seq = [1,2,6,4,3]
# s[i] returns element at given i index
print(seq[2]) # 3
# s[i:j] returns a slice from index i (inclusive) to j (exclusive)
print(seq[1:3]) # [2,6]
# s[i:j:step] # returns a slice with step
print(seq[::4]) # [1,3]
# number of elements in sequence
print(len(seq)) # 5
# min value in sequence
print(min(seq)) # 1
# max value in sequence
print(max(seq)) # 6

# operations for mutable sequences
mseq = [5,2,9,7]
# s[i] = assign new value to element at index i
mseq[2] = 88
print(mseq) # [5,2,88,7]
# s[i:j:step] = iterable replaces slice with iterable
mseq[1:2] = [44,33,11,22]
print(mseq) # [5, 44, 33, 11, 22, 88, 7]
mseq[0:4:2] = [2,2]
print(mseq) # [2, 44, 2, 11, 22, 88, 7]
# del s[i] delete element at index i
del mseq[3]
print(mseq) # [2, 44, 2, 22, 88, 7]
# del s[i:j:step] delete slice
del mseq[2:4]
print(mseq) # [2, 44, 88, 7]

print()

print(''' ------------------ Strings ------------------ ''')
# are immutable
# are iterables

# single/double quotes
str1 = 'hello'
str2 = "hello"

# three single/double quotes (multiline)
str3 = """
        stes
        sdlf
        js;fj
    """
print(str3)

# String Concatenation
"hello" + "world" # helloworld

# String Repetition
# number * "some string"
print(3*"hey!") # hey!hey!hey!
# 0*"string" returns an empty string
print(0*'goodbye')

# transform to uppercase/lowercase
print('upper'.upper())
print('LOWER'.lower())

# returns the number of occurrences of a substring
# accepts optional start/end arguments
# someStr.count(substring, start, end)
print('end occurs', 'endendend'.count('end'), 'time(s) in endendend')

# find first occurrence of substring and returns its index
# accepts optional start/end arguments
# returns -1 if substring is not found
substring = 'end'
substringLength = len(substring)
subIndex = 'never ending story'.find(substring)
print('end can be found at index {} to {}'.format(str(subIndex), str(substringLength + subIndex)))

# return a string which is the concatenation of the strings in a iterable
# the seprator between elements is the string providing the method
# str.join(iterable)
print('1'.join(['b','y','e'])) # b1y1e

# return a copy of the string with all occurrences of the old substring with the new substring
# accepts optional count which is the number of occurrences to replace
# str.replace(old, new, count)
print('newnewnew'.replace('new','old',2)) # oldoldnew

# return a list of the words in the string, using sep as the delimiter string
# if sep is not specified, whitespace are regarded as separators
# maxsplit can be defined to limit the number of splits
# sep and maxsplit are optional
# str.split(sep, maxsplit)
print('1#2#3'.split('#', 1)) # ['1', '2#3']
print('h    e   l  lo'.split()) # ['h', 'e', 'l', 'lo']

multiline = '''hello
good
bye
'''
# return a list of the lines in the string, breaking at line boundaries
print(multiline.splitlines()) # ['hello', 'good', 'bye']

# return a copy of string with trailing/leading characters removed
# accepts optioanl chars argument that specifies the set of characters to be removed
# if chars is not specified, whitespace is removed
# str.rstrip([chars]) remove trailing characters
# str.lstrip([chars]) remove leading characters
print('waiting...   '.rstrip(' .')) # waiting
print('    ...loading'.lstrip()) # ...loading

print()


print(''' ------------------ Lists ------------------ ''')
# like an array
# zero-indexed
# supports negative indices
# dynamically sized
# are mutable
# can contain any kind of object

# new list
newList = list() # constructor
newList = [] # literal
print(list('hello')) # ['h','e','l','l','o']

# concatenate lists
list1 = [5,4]
list2 = [1,7]
print(list1 + list2) # [5, 4, 1, 7]

# list repetition
list3 = [3,5]
print(list3 * 3) # [3, 5, 3, 5, 3, 5]

# list methods
# list(iterable) converts iterable to a list
ltemp = list('1')
print(ltemp) # ['1']
# l.append(x) append to end of list
ltemp.append(3)
print(ltemp)
ltemp.append('good bye')
print(ltemp)
# l.extend(t) adds all elements of a sequence t to the end
ltemp.extend([5,3])
print(ltemp) # ['1', 3, 'good bye', 5, 3]
ltemp.extend('hello')
print(ltemp) # ['1', 3, 'good bye', 5, 3, 'h', 'e', 'l', 'l', 'o'] because strings are sequences, each character is considered an discrete element
# counts occurrences of x in list
print(ltemp.count(3)) # 2
# l.index(x,start,stop) returns index of first occurrence of x
print(ltemp.index(3)) # 1
# l.insert(i,x) insert x at index i
ltemp.insert(3,11111)
print(ltemp) # ['1', 3, 5, 11111, 3]
# l.pop(i) returns element at i and removes it from list. returns last element if index is omitted
print(ltemp.pop(2)) # 5
print(ltemp) # ['1', 3, 11111, 3]
# l.remove(x) removes first occurrence of x
ltemp.remove(3)
print(ltemp) # ['1', 11111, 3]
# l.reverse() reverses items of the list in place
ltemp.reverse()
print(ltemp) # [3, 11111, '1']
# l.sort(cmpfunc,keyf,reverse)
# sort items of l in place. cmpfunc is a comparison. keyf is a key function. reverse is a flag that sorts the list in reverse order
ltemp = [3,590,-89,123]
ltemp.sort(reverse=True)
print(ltemp) # [590, 123, 3, -89]

print()


print(''' ------------------ List Comprehensions ------------------ ''')
# compact way for creating lists
# general form has three components
# list = [(1)expression using a value from an iterable (2)for iterable (3)if conditions]

# create list of even numbers between 2 and 14
listComp = [i for i in range(2,15) if i%2 == 0]
print(listComp)

print()


''' ------------------ Tuples ------------------ '''
# are immutable

newTuple = tuple() # constructor
newTuple = () # literal

# to express one-element tuple, a trailing comma is placed after the element
oneTuple = (55,) 


print(''' ------------------ Mappings/Dictionaries ------------------ ''')
# dictionary
# key/value pair
# unordered (order is not guaranteed)

# new dictionary
newDictionary = dict() # constructor
dictionaryLiteral = {} # literal
dictionaryInitialize = {'my key': 8, 999: 1}

# add pair
newDictionary['key'] = 10
newDictionary['color'] = 'blue'

# number of items in dictionary
print(len(newDictionary)) # 1

# return value using key
# throws KeyError if key not in map
print(newDictionary['key']) # 10

# assignment value to key
newDictionary['color'] = 'red'
print(newDictionary['color']) # red

# delete key/value pair
# throws KeyError if key not in map
del newDictionary['color']
print(newDictionary) # {'key': 10}

# test for key membership in map
# returns boolean value
# key in d
# key not in d
print('key is in dictioanry:', 'key' in newDictionary) # True
print('color is not in dictionary:', 'color' not in newDictionary) # True

# return a shallow copy of a dictionary
newNewDictionary = newDictionary.copy()
print('old', newDictionary)
print('new', newNewDictionary)

newDictionary['key'] = 999
print('old', newDictionary)
print('new', newNewDictionary)

# return a view object of a dictionary's key/value pairs
print(newDictionary.items())

# get list of keys
print(dictionaryInitialize.keys())

# get list of values
print(dictionaryInitialize.values())

# search for key/value
print(99 in dictionaryInitialize) # False
print('my key' in dictionaryInitialize.keys()) # True
print('9' not in dictionaryInitialize.values()) # True

# create a list of keys/values
dictKeys = list(dictionaryInitialize)
print(dictKeys)
dictValues = list(dictionaryInitialize.values())
print(dictValues)

# if key is in the dictionary, remove it and return its value, else return default
# throws KeyError if default is not given and key is not in the dictionary
# dict.pop(key, default)
print('removed key, its value is:', newDictionary.pop('key')) # 999
print(newDictionary.pop('color', 'key does not exist')) # key does not exist

# remove all items from the dictionary
newNewDictionary['color'] = 'aqua'
print(newNewDictionary)
newNewDictionary.clear()
print(newNewDictionary)
print()


print(''' ------------------ Sets ------------------''')
# unordered collection of unique elements (no duplicates)
# can only contain immutable types
# good for checking where an element is contained in the set (membership)
# set (mutable)
# frozenset (immutable)

# set operators
# s1 <= s2 s1 is subset of s2
# s1 < s2 s1 is proper subset of s2
# s1 >= s2 s1 is superset of s2
# s1 > s2 s1 is proper superset of s2
# s1 | s2 the union of s1 and s2
# s1 & s2 the intersection of s1 and s2
# s1 − s2 the set of elements in s1 but not s2
# s1 ˆ s2 the set of elements in precisely one of s1 or s2

# new set
newSet = set()

# set operations
# s.add(x) add x to set 
newSet.add(1)
print(newSet) # {1}
# s.remove(x) remove x from set. raises KeyError if element not in set
newSet.add(56)
newSet.remove(1)
print(newSet) # {56}
# s.discard() remove x from set if present. does not thro error
newSet.discard(55)
print(newSet) # {56}
# s.pop() remove and return an arbitrary element from set. raises KeyError if set if empty
newSet.pop()
# s.clear() remove all elements from set
newSet.add(2)
newSet.add(5)
newSet.add(11)
print(newSet) # {2, 5, 11}
newSet.clear()
print(newSet) # {}
# x in s test x for membership in s
newSet.add(75)
newSet.add(8)
print(8 in newSet) # True
print(1 in newSet) # False
# x not in s test x for non-membership in s
print(1 not in newSet) # True
# find number of elements in set
print('set has', len(newSet), 'element(s)')

print()


''' ------------------- Comments -------------------- '''
# Single line
# use hash sign

''' 
Multiline
use three single quotation marks
'''

""" 
Or
use double quotation marks
"""

print(''' ------------------ Code continuation ---------------------''')
# Use backslash to continue statement on next line
num = 132 \
    + 5
# Or if opening delimiter has not been closed
print(3,
    4,
    5)

print()


print(''' ------------------ Variables ------------------------ ''')
# get memory address
memAddress = 'mem'
print('memory address:', id(memAddress))

# check data type
# type(x) returns type of object x
dtype = 'data'
print(type(dtype))

# reference counting
# how many objects are referencing value/memory location
import sys
ref1 = 777
print('count:', sys.getrefcount(777))
ref2 = 777
print('count:', sys.getrefcount(777))

# delete object
del ref2
print('count:', sys.getrefcount(777))

# casting to another data type
# use constructors
# int()
# float()
# str()
# eval() evaluates to integer or float depending on input
# bin() convert an integer to a binary string

# global variables
# add a global statement to make a variable global
# global someVariable

globalVar = 18
def change():
    global globalVar
    globalVar = 101
    print(globalVar)

change() # 101
print(globalVar) # 101

print()
    

print(''' ------------------ Assignment ------------------ ''')
# identifier (name, variable) = value (object)
numbers = [1,2,3]

# can create an alias (multiple identifiers associated with the same object)
# can access (and change) the underlying object with any assigned identifier/alias
aliasNumber = numbers
aliasNumber.pop()
print(numbers) # [1,2]

# assigning an alias to a new value breaks the binding
aliasNumber = [3,2,1]
aliasNumber.pop()
print(aliasNumber, numbers) # [3,2] [1,2]

temp = 99
atemp = temp
print(temp, atemp) # 99 99
temp = temp + 99 # breaks alias binding
print(temp, atemp) # 198 99

# unpacking (deconstructing)
d1,d2,d3 = 99,88,77
print(d1,d2,d3) # 99 88 77

print()


print(''' ------------------ Instantiation ------------------ ''')
# Creating a new instance of a class
# With class constructor
a = int(5)
print('an integer', a)
# With a literal form (python built in classes)
b = 6
print('another integer', b)

print()


print(''' ------------------ Expressions ------------------ ''')
# has a side effect
# has value

# walrus operator - allows for assignment in the middle of expressions
# name := name some_operation
# print(walrus += 1) will not run
walrus = 101
print(walrus := walrus + 1) # 102

# pythonic swap
# a,b = b,a
swap1 = 'green'
swap2 = 'red'
swap1,swap2 = swap2,swap1
print(swap1, swap2) # red green

print()


''' ------------------ Input ------------------ '''
# input() get input from user. returns a string


''' ------------------ Logical Operators ------------------ '''
# not unary negation
# and conditional and
# or conditional or

# and/or operators short circuit, in that they do not evaluate the
# second operand if the result can be determined based on the value
# of the first operand


print(''' ------------------ Equality Operators ------------------ ''')
# is same identity. checks if aliases are the same object
# is not different identity
# == equivalent. checks for general equivalence
# != not equivalent

a = [5]
b = a
c = [5]
print('check identity between a and b:', a is b) # True
print('check identity between a and c:', a is c) # False
print('check equity between a and c:', a == c) # True

print()


''' ------------------ Comparison Operators ------------------ '''
# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to


''' ------------------ Arithmetic Operators ------------------ '''
# + addition
# - subtraction
# * multiplication
# ** exponent
# / division
# // integer division
# % modulo


''' ------------------ Bitwise Operators ------------------ '''
# ~ bitwise complement
# & bitwise and
# | bitwise or
# ^ bitwise exclusive-or
# << shift bits left, filling in with zeros
# >> shift bits right, filling in with sign bit


print(''' ------------------ Control Statements ------------------ ''')
# if statement
if 1 < 6:
    print(True)

# if-else statement
if 1 > 6:
    print(True)
else:
    print(False)

# if-elif-else statement
grade = 76
if grade > 90:
    print( 'A')
elif grade > 80:
    print('B')
elif grade > 70:
    print('C')
elif grade > 60:
    print('D')
else:
    print('F')

# Ternary Operator 
# a if condition is true else b
isTrue = True if 5 > 12 else False
print(isTrue) # True

# while loop
while_counter = 5
while while_counter > 0:
    print(while_counter * 'good')
    while_counter -= 1

# for loops
# looping through a sequence
for character in 'chocolate':
    print(character)

# index based for loop
# looping 0 to x (exclusive) number of times use range function
for i in range(1,5,3):
    print(i * 'pie')

# options for range
# range([start,] end [, step value])

# break statement exits loop
# continue statement ends current and returns to top of loop

print()


print(''' ------------------ Modules ------------------ ''')
# predefined file with functions/methods
# have to import (loads) them in to use
# there are three ways to import modules

# 1 makes module available but need to use dot syntax to access functions
import math
print(math.sqrt(9))

# 2 import a single function from a module. the function can be used directly without reference the module
from math import sqrt
print(sqrt(9))

# 3 import all functions with wildcard. functions can be used directly
from math import *
print(sqrt(9))

# use dir() to get list of functions available
# print(dir(math))

# use help() describes what each function does
# print(help(math))

# you can create your own functions and modules

print()


print(''' ------------------ Functions ------------------ ''')
# creating a function
# def function_name([parameter list]):
#   code block
#   return statement

def addtwo(x,y):
    return x + y

print(addtwo(5,10)) # 5

# variables in parameter list are local to the function/instance (except for mutable types like lists, its passed by reference)
# can terminate the function with just the return statement without returning a value (or you can have an implicit return by leaving
# out the return statement and the function just "falls off" the last statement and returns to the caller)

print()


print(''' ------------------ Functions/Class Methods ------------------ ''')
# accessors
# returns information about the object but do not change its state

# mutators
# changes the state of the object

numsarr = [4,7,1,88,9,20]
numsarr.sort() # sort function is a mutator method
print(numsarr)


def auglist(l,fnum):
    l.append(101)
    fnum = 222

fnum = 8
nlist = [3,5,2]
auglist(nlist,fnum)
print(nlist) # [3,5,2,101] mutable parameter. nlist and l are aliases to the same object
print(fnum) # 8 fnum parameter is local to the function

print()


print(''' ------------------ built-in sort function ------------------ ''')
# l.sort([key=None, reverse=False])
# takes two optional arguments:
# key specifies a function of one argument that is applied to the list elment before the comparison is made
# reverse specifies that the list should be in reverse order
sortA = ['ONE','two','one','TWO']
sortA.sort()
print(sortA) # ['ONE', 'TWO', 'one', 'two']
sortA.sort(key=str.lower)
print(sortA) # ['ONE', 'one', 'TWO', 'two']
sortA.sort(key=str.lower, reverse=True)
print(sortA) # ['TWO', 'two', 'ONE', 'one']

print()


''' ------------------ File Operations ------------------ '''

# print to file instead of screen
saveFile = open('saved.txt', 'w')
print('save me...', file=saveFile)
print('thanks!', file=saveFile)