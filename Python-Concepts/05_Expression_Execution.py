# String & Numeric Values can operate together with *

A,B = 2,3
Txt = "@"

print(A*Txt*B)

# String & String can operate with + (Concatination)
A,B = "2",3
Txt = "@"
print((A+Txt)*B)

# Numeric Values can operate with +, -, *, /, **, //, %
A,B = 2,3   
c = 4
print(A+B*c) # 2 + 3 * 4 = 14

# Arithmetic Expression with integer and float will result in float
A,B = 2.0,3
c = A*B
print(c) # 2.0 * 3 = 6.0

# Result of division with two integer values will be float
A,B = 2,3
c = A/B
print(c)

# Integer division //  with float and int will result in integer but display as float
A,B = 1.5, 3
c = A//B
print(c, A/B)


# Float gives closest integer value, which is leass than or equal to float value
# Result of (A//B) is same as floor(A/B)
A,B = -12, 5
c = A//B
print(c)

A,B = -12, -5
c = A//B
print(c)

# Remainder (%) is negative when denominator is negative
A,B = -5,2
print(A%B)

C,D = 5,-2
print(C%D)