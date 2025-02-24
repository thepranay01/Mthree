# SQL Learning Day 1

## What is SQL?

Imagine a bookshelf where you store different types of books. SQL works similarly for databases—it helps you store, organize, and find information efficiently.

Your bookshelf has sections (tables) like:

- Fiction
- Science
- History

Each section has shelves (columns) for organizing by:

- Genre (Mystery, Sci-Fi, Biography)
- Author (Agatha Christie, Isaac Asimov, Yuval Noah Harari)
- Language (English, French, Spanish)

If you need to find all science books, instead of searching manually, you can just ask:
📢 "Show me all books where the genre is Science!"

SQL does the same with data—helping you store, manage, and retrieve information efficiently.

## Understanding Rows in SQL

In this analogy, a row represents a specific book in a section (table).

### Example: Books Table (SQL Table)

| ID | Title                   | Genre   | Author          |
| -- | ----------------------- | ------- | --------------- |
| 1  | The Alchemist           | Fiction | Paulo Coelho    |
| 2  | A Brief History of Time | Science | Stephen Hawking |
| 3  | 1984                    | Fiction | George Orwell   |

Each row in the table represents one book with its properties (title, genre, and author).

## SQL Query Example

To find all Science books, you’d use:

```sql
SELECT * FROM Books WHERE Genre = 'Science';
```

👉 This retrieves the row(s) where the genre is Science!

---

## 1. What is a Database?

A database is a structured collection of data that can be easily accessed, managed, and updated. It helps in storing large amounts of information efficiently.

## 2. What is DBMS?

A Database Management System (DBMS) is software that helps users interact with databases. It allows data storage, retrieval, and management.

## 3. Types of DBMS

- **Relational DBMS (RDBMS)** – Uses tables (e.g., MySQL, PostgreSQL).
- **NoSQL DBMS** – Stores data in key-value pairs, documents, or graphs (e.g., MongoDB).

## 4. SQL Example (Finding Mystery Books in 500 Books)

If you have a table named `library` with different book types, you can find all mystery books using SQL:

```sql
SELECT * FROM library WHERE genre = 'Mystery';
```

This selects all rows where the genre column is 'Mystery'.

---

## 5. Table Structure Example (Creating a Library Table)

We can create a table with different book types and categories.

```sql
CREATE TABLE library (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    author VARCHAR(100)
);
```

Each row represents a book, and columns store attributes like title, genre, and author.

---

## 6. Steps to Download MySQL Workbench

To install MySQL Workbench:

1. Visit the MySQL official website.
2. Download and install MySQL Workbench.
3. Connect to the database and start running SQL queries.

Refer to this [guide](https://www.geeksforgeeks.org/how-to-install-sql-workbench-for-mysql-on-windows/) for detailed steps.

---

## 7. DDL (Data Definition Language) Commands

These commands modify database structure.

### Create Table

```sql
CREATE TABLE authors (id INT, name VARCHAR(50), country VARCHAR(50));
```

### Alter Table (Add Column)

```sql
ALTER TABLE authors ADD COLUMN birth_year INT;
```

### Drop Table

```sql
DROP TABLE authors;
```

---

## 8. DML (Data Manipulation Language) Commands

These modify data inside tables.

### Insert Values

```sql
INSERT INTO authors (id, name, country) VALUES (1, 'Mark Twain', 'USA');
```

### Update Data

```sql
UPDATE authors SET country = 'United Kingdom' WHERE id = 1;
```

### Delete Data

```sql
DELETE FROM authors WHERE id = 1;
```

---

## 9. Difference Between TRUNCATE and DELETE

- **DELETE** removes specific rows but allows rollback (undo).
- **TRUNCATE** removes all rows permanently and is faster.

---

## 10. Cloning a Table (Deep Copy vs. Shallow Copy)

### Deep Copy

Copies both the table structure and the data.

```sql
CREATE TABLE new_books AS SELECT * FROM books;
```

### Shallow Copy

Copies only the table structure, but not the data.

```sql
CREATE TABLE new_books LIKE books;
```

🔹 **Think of it like copying a journal:**

- **Deep Copy** → Makes a duplicate with all the notes inside. Any changes in the original journal will not affect the copy.
- **Shallow Copy** → Just copies the empty pages (structure) without any notes (data). If you make changes in the original, they also appear in the copy.

---

## 11. DESC Command (Describe Table)

This command shows the table structure:

```sql
DESC authors;
```

---

## 12. Temporary Tables

Temporary tables store data for a session and disappear after use:

```sql
CREATE TEMPORARY TABLE temp_books AS SELECT * FROM books;
```

---

## 13. Views (Short Explanation)

A **view** is a virtual table based on a query:

```sql
CREATE VIEW best_sellers AS 
SELECT * FROM books WHERE sales > 1000000;
```

---

## 14. DataTypes in MySQL

(Already included in the document)

---

## 15. SQL Query Clauses

Example:

```sql
SELECT name, age FROM employees WHERE age > 30 ORDER BY age DESC;
```

---

## 16. Primary Key, UNIQUE, and NOT NULL Constraints

Example:

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
```
