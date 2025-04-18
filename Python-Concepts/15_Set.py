# Set is the collection of unordered and unindexed elements.
# Set is mutable and does not allow duplicates.
# Set is defined by curly brackets.
# Set is iterable and can be used in loops.
# Each element in the set must be unique and immutable.

nums = {1, 2, 3, 4, 5}
set2 = {1, 2, 2, 3, 4, 5}

# print(nums)  # {1, 2, 3, 4, 5}
print(set2)  # {1, 2, 3, 4, 5} only unique values are printed


collection = {} # this is an empty dictionary not set
collection = set() # this is an empty set
print(type(collection)) # <class 'set'>



# Methods of set

""" 
--> add() - adds an element to the set

--> remove() - removes the specified element from the set

--> pop() - removes an element from the set

--> clear() - removes all elements from the set

--> copy() - returns a shallow copy of the set

--> difference() - returns the difference of two or more sets as a new set

--> difference_update() - removes the items in this set that are also included in another, specified set

--> discard() - removes the specified item

--> intersection() - returns a set that contains all items from both sets

--> union() - returns a set that contains all items from both sets, duplicates are excluded

"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.add(2)  # add 2 to set1

print(set1.intersection(set2))
print(set1.union(set2))

print(set1.difference(set2))