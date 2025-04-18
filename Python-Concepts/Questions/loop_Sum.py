# wap to find the sum of n natural numbers

n = int(input("enter no.: "))

sum = 0
i = 1
while(i<=n):
    sum += i
    i += 1

print(sum)

# using for loop
sum2 = 0
for i in range(1,n+1):
    sum2 += i

print("Sum of Two Numbers is: ", sum)