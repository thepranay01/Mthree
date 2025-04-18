# Find x in tuple

nums = (1, 0, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64

# using for loop
for i in range(0,len(nums)):
    if(nums[i] == x):
        print(x, "is Found at idx: ", i)