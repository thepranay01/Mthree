# Figure out a way to store 9 & 9.0 as separate values in the set.(using built-in data types)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

#second method
values2 = {9, "9.0"}
print(values2)