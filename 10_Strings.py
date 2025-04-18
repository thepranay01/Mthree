#String is data type that stores a sequence of characters.

#concatenation
s = "Hello" + " " + "World"
print(s)

#length of str
s = "Hello World"
print(len(s))

# Escape characters
s = "This is a String with a \"quote\" inside"
t = "This is a String \n with a newline inside" #\t for tab
print(s)
print(t)

# String indexing
s = "Hello World"
print(s[0]) # H
print(s[1]) # e

# Accessing part of a string (slicing)

s = "Hello World"
print(s[0:7])
print(s[:5]) #[0:4]
print(s[6:]) #[6:len(s)]

# Slicing [backward]
str = "This is mr. Pranay"
print(str[-6:-1])

