# Modules in Python
# A module is a file with Python code you can reuse

# Import a built-in module
import math

print(math.pi)          # 3.14159...
print(math.sqrt(16))    # 4.0
print(math.floor(3.8))  # 3
print(math.ceil(3.2))   # 4

# Import just what you need
from random import randint, choice

print(randint(1, 10))              # random number between 1 and 10
print(choice(["rock", "paper", "scissors"]))  # random item

# Import with a shorter alias
import datetime as dt

today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))  # formatted date string

# os module - interact with the operating system
import os

print(os.getcwd())   # current folder
print(os.listdir("."))  # files in current folder

# sys module
import sys

print(sys.version)   # Python version
