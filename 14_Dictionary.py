# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(Changeable) & don't allow duplicate keys

dict_info = {
    "name" : "Pranay",
    "CGPA" : 7.65,
    "Subjects" : ["Python", "C++", "Java", "SQL"],
    "Topics" : ("List", "Tuple", "String", "Dictionary"),
    "is_adult" : True,
    "Section" : "A"
}

# print(dict_info)

# Typecast Dictionary to list
print(list(dict_info.items())) # list of keys



# Dirctory Methods

""" 
1) myDict.keys() ---> returns all keys

2) myDict.values() ---> returns all values

3) myDict.items() ---> returns all key-value pairs as tuples

4) myDict.get(key) ---> returns the value of the specified key

5) myDict.pop(key) ---> removes the element with the specified key

6) myDict.popitem() ---> removes the last inserted key-value pair

7) myDict.clear() ---> removes all elements from the dictionary

8) myDict.copy() ---> returns a copy of the dictionary

9) myDict.update() ---> updates the dictionary with the specified key-value pairs *

"""


print(dict_info["name"]) # error
print(dict_info.get("name")) # no error