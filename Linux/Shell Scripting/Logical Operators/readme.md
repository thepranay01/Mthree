# **Bash Scripting: Logical Operators Explained**

## **Overview**
Logical operators in Bash help control the flow of execution in scripts by evaluating conditions. The most common operators are:
- **AND (`&&`)**: Executes the next command only if the first one succeeds.
- **OR (`||`)**: Executes the next command only if the first one fails.
- **NOT (`!`)**: Negates a condition.

Additionally, Bash supports bitwise operators and other logical constructs like `-a`, `-o`, and `-z` for string and file comparisons.

---

## **Logical Operators in Bash**

| Operator | Description | Example |
|----------|------------|---------|
| `&&` | Logical AND - Executes second command only if the first is successful (exit status 0) | `[ "$a" == "true" ] && echo "a is true"` |
| `||` | Logical OR - Executes second command only if the first fails (non-zero exit status) | `[ "$a" == "true" ] || echo "a is not true"` |
| `!` | Logical NOT - Negates the condition | `[ ! "$a" == "true" ] && echo "a is false"` |
| `-a` | Alternative for `&&` in older scripts (not recommended) | `[ "$a" == "true" -a "$b" == "true" ]` |
| `-o` | Alternative for `||` in older scripts (not recommended) | `[ "$a" == "true" -o "$b" == "true" ]` |
| `-z` | Checks if a string is empty | `[ -z "$var" ] && echo "var is empty"` |
| `-n` | Checks if a string is not empty | `[ -n "$var" ] && echo "var is not empty"` |

---

## **Example: Using Logical Operators in Bash**

```bash
#!/bin/bash

# Reading boolean input from the user
read -p 'Enter a (true/false): ' a
read -p 'Enter b (true/false): ' b

# AND operation
if [[ "$a" == "true" && "$b" == "true" ]]
then
    echo "Both are true."
else
    echo "Both are not true."
fi

# OR operation
if [[ "$a" == "true" || "$b" == "true" ]]
then
    echo "At least one of them is true."
else
    echo "None of them is true."
fi

# NOT operation
if [[ "$a" != "true" ]]
then
    echo "'a' was initially false."
else
    echo "'a' was initially true."
fi

# Checking if a variable is empty using -z
var=""
if [[ -z "$var" ]]
then
    echo "Variable 'var' is empty."
fi

# Checking if a variable is not empty using -n
var="Hello"
if [[ -n "$var" ]]
then
    echo "Variable 'var' is not empty."
fi
```

---

## **Explanation of the Code**
1. The script asks the user for two boolean inputs (`a` and `b`).
2. It performs:
   - AND (`&&`): Checks if both `a` and `b` are `true`.
   - OR (`||`): Checks if at least one of them is `true`.
   - NOT (`!`): Checks if `a` is not `true`.
3. It demonstrates string condition checks with `-z` (empty string) and `-n` (non-empty string).

---

## **Best Practices for Logical Operations in Bash**
- **Prefer `[[ ... ]]` over `[ ... ]`**: The double brackets provide better syntax for conditions.
- **Use proper indentation and comments** to improve script readability.
- **Test conditions with `set -x`**: This helps debug logical expressions in scripts.
- **Avoid using `-a` and `-o`**: They are obsolete and may not work in modern scripts.

---

## **Usage Instructions**
1. Save the script as `logical_operators.sh`.
2. Grant execution permissions:
   ```bash
   chmod +x logical_operators.sh
   ```
3. Run the script:
   ```bash
   ./logical_operators.sh
   ```

---

## **Conclusion**
This guide covers logical operators in Bash scripting, including their syntax, use cases, and best practices. Understanding these operators is crucial for writing efficient shell scripts that make conditional decisions. 🚀