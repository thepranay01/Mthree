# Type Conversion : It is the process of converting one data type into another. It is done automatically by Python. Python automatically converts one data type into another when required. This is called implicit type conversion.

a = 1
b = 4.25

sum = a+b # 2.0+4.25 = 5.25
print("Sum of a and b is: ", sum) # 5.25



# Type Casting : It is the process of converting one data type into another. It is done explicitly by the user. The user can use the built-in functions to convert one data type into another.

a,b = 1, "2"
# print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# To fix this, we can use type casting to convert the string to an integer.
b = int(b) # Convert b to int
print(a+b)

val = input("Enter a number: ") 
print(type(val), val)