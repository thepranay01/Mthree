# A built-in data type that lets us create immutable sequences of Values.

tup = (87, 65, 98, 34, 89)
#tup[0] = 43 # Not allowed in python

tup1 = ()
tup2 = (1,)
tup3 = (1,2,3)

# type of tup
print(type(tup))

#slicing
print(tup[1:3])

#Tuple Methods
""" 
.index(el) ---> returns index of first occurrence
.count(el) ---> returns total occurrences
"""

