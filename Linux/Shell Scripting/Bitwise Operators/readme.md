# **Bash Scripting: Bitwise Operators Explained**

## **Overview**
Bitwise operators in Bash perform operations at the binary level, manipulating individual bits of integer values.

### **Bitwise Operators:**
- **AND (`&`)**: Performs bitwise AND.
- **OR (`|`)**: Performs bitwise OR.
- **XOR (`^`)**: Performs bitwise XOR.
- **Complement (`~`)**: Performs bitwise negation.
- **Left Shift (`<<`)**: Shifts bits to the left.
- **Right Shift (`>>`)**: Shifts bits to the right.

---

## **Bitwise Operators in Bash**

| Operator | Description | Example |
|----------|------------|---------|
| `&` | Bitwise AND | `echo $(( a & b ))` |
| `|` | Bitwise OR | `echo $(( a | b ))` |
| `^` | Bitwise XOR | `echo $(( a ^ b ))` |
| `~` | Bitwise Complement | `echo $(( ~a ))` |
| `<<` | Left Shift | `echo $(( a << 1 ))` |
| `>>` | Right Shift | `echo $(( b >> 1 ))` |

---

## **Example: Using Bitwise Operators in Bash**

```bash
#!/bin/bash

# Reading integer input from the user
read -p 'Enter an integer a: ' a
read -p 'Enter an integer b: ' b

echo "Bitwise AND of a and b is $(( a & b ))"
echo "Bitwise OR of a and b is $(( a | b ))"
echo "Bitwise XOR of a and b is $(( a ^ b ))"
echo "Bitwise Complement of a is $(( ~a ))"
echo "Left Shift of a is $(( a << 1 ))"
echo "Right Shift of b is $(( b >> 1 ))"
```

---

## **Expected Output**
### **Input:**
```
Enter an integer a: 5
Enter an integer b: 3
```

### **Output:**
```
Bitwise AND of a and b is 1
Bitwise OR of a and b is 7
Bitwise XOR of a and b is 6
Bitwise Complement of a is -6
Left Shift of a is 10
Right Shift of b is 1
```

---

## **Best Practices for Bitwise Operations in Bash**
- **Use integers only**: Bitwise operators work on integer values.
- **Use parentheses `(( ... ))` for arithmetic expansion**: This ensures proper evaluation of expressions.
- **Test operations carefully**: Unexpected results may occur due to signed integer representation.
- **Combine with logical conditions if necessary**: Bitwise operations are useful for flags and bitmasking.

---

## **Usage Instructions**
1. Save the script as `bitwise_operators.sh`.
2. Grant execution permissions:
   ```bash
   chmod +x bitwise_operators.sh
   ```
3. Run the script:
   ```bash
   ./bitwise_operators.sh
   ```

---

## **Conclusion**
This guide provides an understanding of bitwise operators in Bash scripting, including their syntax, use cases, and best practices. These operators are fundamental in performing low-level binary operations. 🚀