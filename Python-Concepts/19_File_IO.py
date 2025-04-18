# Python can be used to perform file operations such as reading, writing, and appending to files.
# Types of files include text files(.txt, .docx, .log, etc), binary files(.mp4, .mov, .png, etc), and CSV files.
""" 
f = open("file_name", "mode")

mode ---> "r" (read), "w" (write), "a" (append), 

operations ---> read(), write(), append(), close(), readline(), readlines(),
data = f.read()
f.close() # Closes the file

"""
# The most common file operations are:

# 1. Opening a file
file = open("example.txt", "r")  # Opens the file in read mode

# 2. Reading a file
file = open("example.txt", "r")  # Opens the file in read mode
content = file.read()
print(content)  # Prints the content of the file

# 3. Writing to a file
file = open("example.txt", "w")  # Opens the file in write mode
file.write("Hello, World!")  # Writes to the file

# 4. Appending to a file
file = open("example.txt", "a")  # Opens the file in append mode
file.write("\nAppending this line.")  # Appends to the file

# 5. Closing a file
file = open("example.txt", "r")  # Opens the file in read mode
content = file.read()
file.close()  # Closes the file

# 6. Deleting a file
import os
os.remove("example.txt")  # Deletes the file

# 7. Renaming a file
os.rename("old_name.txt", "new_name.txt")  # Renames the file

# 8. Copying a file
import shutil
shutil.copy("source.txt", "destination.txt")  # Copies the file

# 9. Moving a file
shutil.move("source.txt", "destination_folder/")  # Moves the file

# 10. Checking if a file exists
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")
    
# 11. Getting file information
import os
file_info = os.stat("example.txt")  # Gets file information
print(file_info)  # Prints file information

# 12. Reading and writing CSV files
import csv
with open("example.csv", "r") as csvfile:
    reader = csv.reader(csvfile)  # Reads the CSV file
    for row in reader:
        print(row)  # Prints each row of the CSV file
with open("example.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)  # Writes to the CSV file
    writer.writerow(["Name", "Age"])  # Writes the header
    writer.writerow(["Alice", 30])  # Writes a row of data
    writer.writerow(["Bob", 25])  # Writes another row of data

    
# 13. Reading and writing JSON files
import json
data = {"name": "Alice", "age": 30}  # Sample data
with open("example.json", "w") as jsonfile:
    json.dump(data, jsonfile)  # Writes the JSON data to a file
with open("example.json", "r") as jsonfile:
    data = json.load(jsonfile)  # Reads the JSON data from a file
    print(data)  # Prints the JSON data
    
    
# 14. Reading and writing XML files
import xml.etree.ElementTree as ET
data = ET.Element("data")  # Creates an XML element


# 15. Reading and writing Excel files
import pandas as pd
data = {"Name": ["Alice", "Bob"], "Age": [30, 25]}  # Sample data
df = pd.DataFrame(data)  # Creates a DataFrame
df.to_excel("example.xlsx", index=False)  # Writes the DataFrame to an Excel file
df = pd.read_excel("example.xlsx")  # Reads the Excel file into a DataFrame