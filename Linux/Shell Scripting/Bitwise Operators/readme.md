# **Bash Scripting: Bitwise Operators Explained**

## **Overview**
Bitwise operators in Bash perform operations at the binary level, manipulating individual bits of integer values. These operators are essential for tasks that require direct manipulation of binary data, such as setting flags, performing bit masking, and optimizing performance in low-level programming.

### **Bitwise Operators:**
- **AND (`&`)**: Performs bitwise AND. Useful for masking bits.
- **OR (`|`)**: Performs bitwise OR. Useful for setting bits.
- **XOR (`^`)**: Performs bitwise XOR. Useful for toggling bits.
- **Complement (`~`)**: Performs bitwise negation. Inverts all bits.
- **Left Shift (`<<`)**: Shifts bits to the left. Useful for multiplying by powers of two.
- **Right Shift (`>>`)**: Shifts bits to the right. Useful for dividing by powers of two.

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

### **Detailed Examples:**
- **Bitwise AND (`&`)**:
    ```bash
    a=5  # 0101 in binary
    b=3  # 0011 in binary
    echo $(( a & b ))  # 0001 in binary, which is 1
    ```
- **Bitwise OR (`|`)**:
    ```bash
    a=5  # 0101 in binary
    b=3  # 0011 in binary
    echo $(( a | b ))  # 0111 in binary, which is 7
    ```
- **Bitwise XOR (`^`)**:
    ```bash
    a=5  # 0101 in binary
    b=3  # 0011 in binary
    echo $(( a ^ b ))  # 0110 in binary, which is 6
    ```
- **Bitwise Complement (`~`)**:
    ```bash
    a=5  # 0101 in binary
    echo $(( ~a ))  # 1010 in binary (two's complement), which is -6
    ```
- **Left Shift (`<<`)**:
    ```bash
    a=5  # 0101 in binary
    echo $(( a << 1 ))  # 1010 in binary, which is 10
    ```
- **Right Shift (`>>`)**:
    ```bash
    b=3  # 0011 in binary
    echo $(( b >> 1 ))  # 0001 in binary, which is 1
    ```

---

## **Example: Using Bitwise Operators in Bash**

```bash
#!/bin/bash

# Reading integer input from the user
read -p 'Enter an integer a: ' a
read -p 'Enter an integer b: ' b

# Perform bitwise operations and display results
echo "Bitwise AND of a and b is $(( a & b ))"  # AND operation
echo "Bitwise OR of a and b is $(( a | b ))"   # OR operation
echo "Bitwise XOR of a and b is $(( a ^ b ))"  # XOR operation
echo "Bitwise Complement of a is $(( ~a ))"    # Complement operation
echo "Left Shift of a is $(( a << 1 ))"        # Left shift operation
echo "Right Shift of b is $(( b >> 1 ))"       # Right shift operation