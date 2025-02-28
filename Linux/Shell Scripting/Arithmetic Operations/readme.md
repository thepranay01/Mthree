# **Bash Script for Arithmetic Operations**

## **Overview**
This Bash script performs basic arithmetic operations such as addition, subtraction, multiplication, division, modulus, increment, and decrement.

---

## **Code**
```bash
#!/bin/bash

# Reading data from the user
read -r -p "Enter a: " a
read -r -p "Enter b: " b

# Performing arithmetic operations
add=$((a+b))
echo "Addition of a and b is: ${add}"

sub=$((a-b))
echo "Subtraction of a and b is: ${sub}"

mul=$((a*b))
echo "Multiplication of a and b is: ${mul}"

div=$((a/b))
echo "Division of a and b is: ${div}"

mod=$((a%b))
echo "Modulus of a and b is: ${mod}"

# Increment and Decrement operations
((++a))
echo "Increment operator when applied on a results in: ${a}"

((--b))
echo "Decrement operator when applied on b results in: ${b}"
```

---

## **Explanation**
| Operator | Description |
|----------|------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus (Remainder) |
| `++` | Increment |
| `--` | Decrement |

---

## **Usage**
1. Save the script as **`arithmetic_operations.sh`**.
2. Provide execution permissions using:
   ```bash
   chmod +x arithmetic_operations.sh
   ```
3. Run the script using:
   ```bash
   ./arithmetic_operations.sh
   ```
---

## **Best Practices**
- Use `-r` with `read` to prevent backslash interpretation.
- Enclose variables in `${}` to ensure proper expansion.
- Use `(( ))` for arithmetic operations instead of `expr`.

---

This script efficiently demonstrates basic arithmetic operations in Bash. 🚀
