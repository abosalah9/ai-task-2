#!/usr/bin/env python
# coding: utf-8

# **1-Write a Python program to calculate the length of a string using 2 ways

# In[8]:


a='welcome'
print(len(a))


# In[ ]:


a='welcome'
count=0
for i in a :
    count=count+1
print(count)


# **2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead ("##Sample String : 'w3resource'
# Expected Result : 'w3ce'
# ##Sample String : 'w3'
# Expected Result : 'w3w3'
# ##Sample String : ' w'
# Expected Result : Empty String)

# In[ ]:


a=input('inter a string')
if(len(a)>=2):
    string=str(a[0:2]+a[(len(a)-2):(len(a))])
    print(string)
else:
    print('empty string: ')


# **3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc'
# Expected Result : 'abcing')

# In[ ]:


a=str(input('inter a string'))
if(len(a)>=3):
    stringend=str(a[(len(a)-3):(len(a))])
    if (stringend!='ing'):
        print(a+'ing')
    else:
        print(a+'ly')
else:
    print(a)


# **4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# (Longest word: Exercises
# Length of the longest word: 9)

# In[ ]:


longest_word = ''
longest_length = 0
word_list = ["Python", "Exercises", "Function", "Longest", "Word"]
for word in word_list:
    word_length = len(word)
    if word_length > longest_length:
        longest_word = word
        longest_length = word_length

print( 'longest word is ', longest_word  )
print('length of longest word is', length_longest_word)


# **5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged using 2 ways (Sample String:abca  Expected Result:ebce)

# In[ ]:


string_one = input("enter first string ")
string_two = input("enter second string ")
new_string = string_two[:2]+string_one[2:]+' '+string_one[:2]+string_two[2:]
print(new_string)


# In[ ]:





# **6-Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)

# In[ ]:


name='ali magdi'
print(name[0::2]


# **7-Write a Python program to count the occurrences of each word in a given sentence (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)

# In[ ]:


string='my name is ali , i love my name very much'
words=string.split()
for i in words:
    print(i,string.count(i))
    
  


# **8-Write a Python script that takes input from the user and displays that input back in upper and lower cases

# In[ ]:


my_string = input("enter something ")

print(my_string.upper())
print(my_string.lower())


# **9-Write a Python function to reverse a string if its length is a multiple of 4

# In[ ]:


name=input()
if len(name)%4==0 :
    print(name[::-1])
else:
    print(name)


# **10- Write a Python program to remove a newline in Python

# In[ ]:





# **11-Write a Python program to check whether a string starts with specified characters

# In[ ]:


name=input()
chs=['A','X','W']
if name[0] in chs:
    print('yes')
else:
    print('no')


# **12- Write a Python program to add prefix text to all of the lines in a string

# In[ ]:





# **13-Write a Python program to print the following numbers up to 2 decimal places

# In[ ]:


my_float = float(input("enter a float number "))

print("this is a float number %.2f" % my_float)


# **14-Write a Python program to print the following numbers up to 2 decimal places with a sign

# In[ ]:


my_float = float(input("enter a float number "))

print("this is a float number %+.2f" % my_float)


# **15-Write a Python program to display a number with a comma separator

# In[ ]:


my_int = int(input("enter a number "))

print('{:,}'.format(my_int))


# **16-Write a Python program to reverse a string using 2 ways

# In[ ]:


my_sentence = input("enter a sentence ")

my_list = my_sentence.split()
print(' '.join(my_list[::-1]))


#  **17-Write a Python program to count repeated characters in a string (hint:use dictionary)

# In[ ]:


myd=dict()
for i in chs:
    myd[i]=name.count(i)
    print(myd)


# **18-Write a Python program to find the first non-repeating character in a given string

# In[ ]:


name='aabbccgkkhgfddfdgg'
for ch in name:
    if name.count(ch)==1:
        print(ch)
        break


# **19-Write a Python program to remove spaces from a given string

# In[ ]:


name='ali osama mohamed '
newname=name.replace('','')
print(newname)


# **20-Write a Python program to count the number of non-empty substrings of a given string

# In[ ]:





# **21-write a Python program to swap first and last element of any list.

# In[ ]:


l=['ahmed','ali','maher']
l[0],l[-1]=l[-1],l[0]
print(l)


# **22-Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90])

# In[ ]:


l=[1,2,3,4]
pos1=int(input())
pos2=int(input())
l[pos1] ,l[pos2]=l[pos2] ,l[pos1]
print(l)


# **23- search for the all ways to know the length of the list

# In[ ]:


**24-write a Python code to find the Maximum number of list of numbers.


# In[ ]:


l=[1,2,3,4,5,7]
print(max(l))


# In[ ]:


**25-write a Python code to find the Minimum number of list of numbers.


# In[ ]:


l=[1,2,3,4,5,7]
print(min(l))


# **26-search for if an elem is existing in list

# In[ ]:


l=[1,2,3,'ali']
l.index(3)
l.index('ali')
l.index('ahmed')


# **27- clear python list using different ways

# In[ ]:


l=[1,2,3,4]
l.clear()
print(l)
del(l[:])
print(l)


# **28-remove duplicated elements from a list

# In[ ]:


l=[1,2,5,2,4,3,13,4,3]
a=set(l)
print(a)
b=list(a)
print(b)


# **29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries. (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])

# In[ ]:


d


# **30-write a python program to count unique values inside a list using different ways

# In[ ]:


l=[1,4,3,3,6,7,8,9,3,2,1]
l.count(3)


# **31-write a python program Extract all elements with Frequency greater than K (Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] )

# In[ ]:





# **32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5)

# In[ ]:


def find_strongest_neighbor(arr):
    result = []
    n = len(arr)

    for i in range(1, n - 1):
        strongest_neighbor = max(arr[i - 1], arr[i + 1])
        result.append(strongest_neighbor)

    return result

# Input list
input_list = list(map(int, input("Enter space-separated numbers: ").split()))

strongest_neighbors = find_strongest_neighbor(input_list)
print("Output:", " ".join(map(str, strongest_neighbors)))


# **33-write a Python Program to print all Possible Combinations from the three Digits (Input: [1, 2, 3]
# Output:
# 1 2 3 ##
# 1 3 2 ##
# 2 1 3 ##
# 2 3 1 ##
# 3 1 2 ##
# 3 2 1)

# In[ ]:





# **34-write a Python program to find all the Combinations in the list with the given condition (Input: test_list = [1,2,3] 
# Output: 
#  [1], [1, 2], [1, 2, 3], [1, 3]
#  [2], [2, 3], [3])

# In[ ]:


)


# **35-write a Python program to get all unique combinations of two Lists (List_1 = ["a","b"]
# List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )

# In[ ]:





# **36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1 
# 
# **Output : 2 3 4 5 2)

# In[ ]:


def remove_element_from_list(lst, element_to_remove):
    return [item for item in lst if item != element_to_remove]

# Example input
input_list = [1, 1, 2, 3, 4, 5, 1, 2, 1]
element_to_remove = 1

# Removing all occurrences of the element
output_list = remove_element_from_list(input_list, element_to_remove)

# Displaying the output
print(output_list)  # Output: [2, 3, 4, 5, 2]


# **37-write a python program to Replace index elements with elements in Other List (The original list 1 is : [‘Gfg’, ‘is’, ‘best’] The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])

# In[ ]:





# **38- write python program to Retain records with N occurrences of K(Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
# Output : [(4, 5, 5, 4)]
# Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 
# Output : [] )

# In[ ]:





# **39-write a Python Program to Sort the list according to the column using lambda
# array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Output :
# Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]]
# Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]

# In[ ]:


array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]

def sort_by_column(col_index):
    return sorted(array, key=lambda x: x[col_index])

columns = len(array[0])

for i in range(columns):
    sorted_array = sort_by_column(i)
    print(f"Sorted array specific to column {i}, {sorted_array}")


# In[ ]:


**40- write a program to Sort Python Dictionaries by Key or Value
Input:
{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

Output: 
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}


# In[ ]:





# **41-write python program to Remove keys with Values Greater than K ( Including mixed values )
# nput : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’},
# K = 7 
# Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}

# In[ ]:


def remove_keys_greater_than_K(test_dict, K):
    keys_to_remove = []

    for key, value in test_dict.items():
        if isinstance(value, (int, float)) and value > K:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        test_dict.pop(key)

    return test_dict

# Test the function
test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
K = 7
result_dict = remove_keys_greater_than_K(test_dict, K)
print(result_dict)


# **42-Write a Python program to concatenate the following dictionaries to create a new one
# 
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# In[ ]:


def concatenate_dicts(*dicts):
    result_dict = {}
    for d in dicts:
        result_dict.update(d)
    return result_dict

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result_dict = concatenate_dicts(dic1, dic2, dic3)

print(result_dict)


# **43-Write a Python program to iterate over dictionaries using for loops

# In[ ]:





# **44- Write a Python script to merge two Python dictionaries

# In[ ]:





# **45-Write a Python program to get the maximum and minimum values of a dictionary values

# In[ ]:





# **46- Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# In[ ]:





# **47-Write a Python program to create a tuple of numbers and print one item

# In[ ]:





# **48-Write a Python program to unpack a tuple into several variables

# In[ ]:





# **49-Write a Python program to add an item to a tuple

# In[ ]:





# **50-Write a Python program to convert a tuple to a string

# In[ ]:





# **51-Write a Python program to convert a list to a tuple

# In[ ]:





# **52-Write a Python program to reverse a tuple

# In[ ]:





# **53-Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# In[ ]:





# **54-Write a Python program to convert a given string list to a tuple
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

# In[ ]:





# **55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples

# In[ ]:


a=(1,2,3)
b=sum(a)/len(a)
print(b)


# **56-Write a Python program to add member(s) to a set.

# In[ ]:


a={1,2,3}
a.add(4)
print(a)


# **57-Write a Python program to remove an item from a set if it is present in the set.

# In[ ]:





# **58-Write a Python program to create an intersection,union,difference and symmetric difference of sets

# In[ ]:





# **59-Write a Python program to find the maximum and minimum values in a set

# In[ ]:


a={1,2,3}
print(max(a))
print(min(a))


# **60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# In[ ]:




