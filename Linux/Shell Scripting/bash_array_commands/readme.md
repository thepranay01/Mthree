# **Bash Array Commands – Structured Documentation**

## **1. Declaring a Static Array**
```bash
arr=("Jayesh" "Shivang" "1" "Vipul" "Nishant" "2")
```
- Declares an array named **`arr`** containing **string and numeric values**.
- Elements are enclosed in **parentheses ()**, separated by spaces.

---

## **2. Printing All Elements of the Array**
```bash
echo "All elements of the array:"
echo "${arr[@]}"  # Prints all elements
echo "${arr[*]}"  # Prints all elements
```
- `@` and `*` both return **all elements** in the array.

---

## **3. Printing the First Element**
```bash
echo "The first element:"
echo "${arr[0]}"
```
- Arrays in Bash are **zero-indexed**, so **`${arr[0]}`** returns the first element.

---

## **4. Printing an Element at a Selected Index**
```bash
selected_index=3
echo "Selected index element at index $selected_index:"
echo "${arr[$selected_index]}"
```
- The variable **`selected_index`** stores the index.
- **`${arr[$selected_index]}`** prints the element at **index 3**.

---

## **5. Printing Elements from a Particular Index**
```bash
echo "Elements from a particular index:"
echo "${arr[@]:2}"  # Prints elements starting from index 2
echo "${arr[*]:2}"  # Prints elements starting from index 2
```
- **`${arr[@]:2}`** extracts all elements **starting from index 2**.
- **`${arr[*]:2}`** does the same.

---

## **6. Printing Elements Within a Range**
```bash
echo "Elements in a range:"
echo "${arr[@]:1:3}"  # Prints elements from index 1 to 3
echo "${arr[*]:1:3}"  # Prints elements from index 1 to 3
```
- **`${arr[@]:1:3}`** extracts **3 elements starting from index 1**.
- **`${arr[*]:1:3}`** does the same.

---

## **Summary Table**
| Command | Description |
|---------|------------|
| `arr=("Jayesh" "Shivang" "1" "Vipul" "Nishant" "2")` | Declares a static array |
| `echo "${arr[@]}"` | Prints all elements of the array |
| `echo "${arr[*]}"` | Prints all elements of the array |
| `echo "${arr[0]}"` | Prints the first element |
| `echo "${arr[$selected_index]}"` | Prints the element at a specific index |
| `echo "${arr[@]:2}"` | Prints elements from index 2 onward |
| `echo "${arr[@]:1:3}"` | Prints 3 elements starting from index 1 |

---

This document provides a **clear and structured** explanation of how **Bash arrays** work and how elements can be accessed, printed, and manipulated. 🚀
