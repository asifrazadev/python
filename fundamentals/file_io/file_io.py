# File I/O in Python

# --- Writing a file ---
with open("notes.txt", "w") as f:
    f.write("Hello!\n")
    f.write("This is line 2.\n")

print("File written.")

# --- Reading a file ---
with open("notes.txt", "r") as f:
    content = f.read()

print(content)

# --- Append to a file ---
with open("notes.txt", "a") as f:
    f.write("This line was added later.\n")

# --- Read line by line ---
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# --- Check if file exists ---
import os

if os.path.exists("notes.txt"):
    print("file exists")
else:
    print("file not found")

# --- Delete the file ---
os.remove("notes.txt")
print("file deleted")
