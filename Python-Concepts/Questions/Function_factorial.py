n = int(input("Enter number: "))

def fact(num):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

ans = fact(n)
print(ans)