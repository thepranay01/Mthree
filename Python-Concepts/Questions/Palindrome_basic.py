# WAP to check if a list contains a palindrome of elements.

ls = [1, "abc", "abc", 1]

cp = ls.copy()
cp.reverse()


if(ls == cp):
    print("True")

else :
    print("False")