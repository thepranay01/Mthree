str = "I am a string"

str.endswith("ing") # True
str.endswith("str") # False

str.startswith("I") # True
str.startswith("a") # False

# capitalize() - Capitalizes the first character of the string and lowercases the rest
str.capitalize()

# replace() - Replaces a substring with another substring
str.replace("string", "string2")

# find() - Returns the index of the first occurrence of a substring in the string
str.find("a") # 2
str.find("x") # -1 (not found)

# rfind() - Returns the index of the last occurrence of a substring in the string
str.rfind("a") # 2

# find length of string
