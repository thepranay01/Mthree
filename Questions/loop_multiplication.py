# Print the multiplication table of a number n.

n = int(input("Enter Your Number: "))

# using while loop
i = 1
while i<=10:
    print(n,"x",i,"=", n*i)
    i = i + 1
    
# using for loop
for i in range(1,11):
    print(n,"x",i,"=", n*i)