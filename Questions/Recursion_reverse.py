# print n to 1 recursively
def rev(n):
    if(n == 0):
        return
    print(n, end = " ")
    rev(n-1)

rev(10)