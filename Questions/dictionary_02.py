# WAP to enter marks of 3 subjects from user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

dict = {}

subject1 = int(input("Enter Marks of Hindi: "))
dict.update({"Hindi": subject1})

subject2 = int(input("Enter Marks of English: "))
dict.update({"English": subject2})

subject3 = int(input("Enter Marks of Maths: "))
dict.update({"Maths": subject3})

print(dict)