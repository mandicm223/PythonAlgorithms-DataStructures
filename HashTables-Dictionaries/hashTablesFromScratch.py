'''
Problem Statement - Python Dictionaries and Hash Tables
In this assignment, you will recreate Python dictionaries from scratch using data structure called hash table. 
Dictionaries in Python are used to store key-value pairs. Keys are used to store and retrieve values. 
For example, here's a dictionary for storing and retrieving phone numbers using people's names.
'''

phone_numbers = {
  'Aakash' : '9489484949',
  'Hemanth' : '9595949494',
  'Siddhant' : '9231325312'
}

# insert new
phone_numbers['Vishal'] = 8787878787

# update 
phone_numbers['Aakash'] = 7878787878

# iterating through dictionarie 
for name in phone_numbers:
    print('Name' , name  , 'Phone number' , phone_numbers[name])


'''
Dictionaries in Python are implemented using a data structure called hash table. 
A hash table uses a list/array to store the key-value pairs,
and uses a hashing function to determine the index for storing or retrieving the data associated with a given key.
'''


'''
Data List
We'll build the HashTable class step-by-step. 
As a first step is to create a Python list which will hold all the key-value pairs. We'll start by creating a list of a fixed size.
'''

MAX_HASHTABLE_SIZE = 4096
data_list = [None] * 4096

'''
Your objective in this assignment is to implement a HashTable class which supports the following operations:

Insert: Insert a new key-value pair
Find: Find the value associated with a key
Update: Update the value associated with a key
List: List all the keys stored in the hash table
The HashTable class will have the following structure (note the function signatures):

class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass
    
    def find(self, key):
        """Find the value associated with a key"""
        pass
    
    def update(self, key, value):
        """Change the value associated with a key"""
        pass
    
    def list_all(self):
        """List all the keys"""
        pass
'''

'''
Hashing Function
A hashing function is used to convert strings and other non-numeric data types into numbers, which can then be used as list indices.
For instance, if a hashing function converts the string "Aakash" into the number 4,
then the key-value pair ('Aakash', '7878787878') will be stored at the position 4 within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

Iterate over the string, character by character
Convert each character to a number using Python's built-in ord function.
Add the numbers for each character to obtain the hash for the entire string
Take the remainder of the result with the size of the data list
'''

def get_index(data_list , a_string):
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
    
    list_index = result % len(data_list)
    return list_index

idnex = get_index(data_list , 'Don O Leary')
print(idnex == 941)


'''
Insert
To insert a key-value pair into a hash table, we can simply get the hash of the key, and store the pair at that index in the data list.

data_list[get_index(data_list , 'Hemanth')] = ('Hemanth' , 9595959494)
'''

'''
Find
The retrieve the value associated with a pair, we can get the hash of the key and look up that index in the data list.

idx = get_index(data_list , 'Aakash')
key , value = data_list[idx]
'''

'''
List
To get the list of keys, we can use a simple list comprehension.

keys = [  kv[0] for kv in data_list if kv is not None  ] 
'''


class BasicHashTable:
    def __init__(self , max_size=MAX_HASHTABLE_SIZE):
        self.data_list = [None] * max_size
    
    def insert(self , key , value):
        idx = get_index(self.data_list , key)
        self.data_list[idx] = key , value
    
    def find(self , key):
        idx = get_index(self.data_list , key)

        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key , value = kv
            return value
    
    def update(self , key , value):
        idx = get_index(self.data_list , key)

        self.data_list[idx] = key , value
    

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024)

# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
first_find = basic_table.find('Hemanth')
print(first_find)


# Update a value
basic_table.update('Aakash', '7777777777')

# Check the updated value
first_update = basic_table.find('Aakash')
print(first_update)

print(basic_table.list_all())

'''
As you can see above, the value for the key listen was overwritten by the value for the key silent. Our hash table implementation is incomplete because it does not handle collisions correctly.

To handle collisions we'll use a technique called linear probing. Here's how it works:

While inserting a new key-value pair if the target index for a key is occupied by another key, then we try the next index, 
followed by the next and so on till we the closest empty location.

While finding a key-value pair, we apply the same strategy, but instead of searching for an empty location, 
we look for a location which contains a key-value pair with the matching key.

While updating a key-value pair, we apply the same strategy, but instead of searching for an empty location, 
we look for a location which contains a key-value pair with the matching key, and update its value.

We'll define a function called get_valid_index, 
which starts searching the data list from the index determined by the hashing function get_index and returns the first index which is 
either empty or contains a key-value pair matching the given key.
'''

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list , key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if key == k: 
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


'''
data_list2 = [None] * MAX_HASHTABLE_SIZE
print(get_valid_index(data_list2, 'listen') == 655)
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)
print(get_valid_index(data_list2, 'silent') == 656)
'''

class ProbingHashTable:
    def __init__(self , max_size = MAX_HASHTABLE_SIZE):
        self.data_list = None * max_size

    def insert(self , key , value):
        idx = get_valid_index(self.data_list , key)
        self.data_list[idx] = (key , value)

    def find(self , key):
        idx = get_valid_index(self.data_list , key)

        kv = self.data_list[idx]

        return None if kv is None else kv[1]
    
    def update(self , key , value):
        idx = get_valid_index(self.data_list , key)
        self.data_list[idx] = ( key , value)

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
