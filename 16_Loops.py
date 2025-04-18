# Loops are used to repeat instructions

# while loop
count = 1
while count <= 5 :
    print("hello")
    count += 1
    
    
# For loop
for i in range(0,5):
    print("World")
    
# or
nums = [1, 2, 3, 4, 5, 6, 7]
for val in nums:
    print(val)
    
print("End of Loop")    
    
# Break : used to terminate the loop when encountered 

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
    
print("End of Loop")

# continue : terminates execution in the current iteration & continues execution of the loop with the next iteration

i = 1
while i <= 5:
    
    if(i <= 3):
        i += 1
        continue
    print(i)
    i += 1


# range()
# range(start?, stop, step?)

#-> Pass Statement : pass is a null statement that does nothing. It is used as a placeholder for future code.
