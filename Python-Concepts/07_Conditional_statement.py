a = int(input("a: "))
b = int(input("b: "))

if(a<b) :
    print(a * b) # INDENTATION-> Proper spacing 4 spaces here

elif (a>b) :
    print(a / b)

else :
    print(a + b)

print("Code 01 is ended")



# Traffic Lights

"""
Red -> Stop
Yellow -> Look
Green -> Go
other color -> Light is Broken

"""

light = input("Color of light: ")

if(light == "red"):
    print("Stop")

elif(light == "Yellow"):
    print("Look")

elif(light == "Green"):
    print("Go")

else:
    print("Light is Broken")
    
print("Code 02 is ended")


#Grades of Student

marks = int(input("Enter Marks: "))

if(marks >= 90):
    print("A")

elif(marks>= 80 and marks<90):
    print("B")

elif(marks >= 70 and marks< 80):
    print("C")

else:
    print("D")
    


# Single Line if (Ternary Operator)
food = input("Food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)

# without variable eat
# <statement 01> if<Condition> else <Statement 02>

print("Sweet") if(food == "cake") or (food == "Jalebi") else print("not sweet")

# Clever if
# <variable> = (False_val, true_value) [<condition>]

age = int(input("age : "))
vote = ("Yes", "No") [age < 18]
print(vote)