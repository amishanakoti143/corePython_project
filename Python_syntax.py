# Topic: Basic Syntax and Print Statement
# Author: Amisha Nakoti .

#------------------------------------------------------------------------ 
# Python Syntax Basics
# ------------------------
# Python uses indentation (whitespace) to define blocks of code.
# Each block of code (like loops, functions, conditionals)
#  must be consistently indented.

#-----------------------------------------------------------------------

# Valid indentation example: #✅
if True:
    print("This line is indented correctly.")

# Invalid indentation would raise an error:   ❌
if True:
print("This would cause an IndentationError")
#------------------------------------------------------------------------------
# ---------------------------
# The print() Function
# ---------------------------
# print() is used to display output on the screen

print("Hello, World!")
print("Python is Easy to learn")

# ---------------------------
# Printing Multiple Items
# ---------------------------
name = "S"
age = 25
print("My name is", name, "and I am", age, "years old.")

# ---------------------------
# Escape Characters (\n)  .... to new line
# ---------------------------
print("This is a line break\nNext line starts here.")
print("He said, \"Python is great!\"")

# ---------------------------
# Comments
# ---------------------------
# Single-line comment  [we use # to comment  single line]

#multi-line comment  
#  [To write a multiline comment in Python, we use triple quotes — either 
#      """  """   or '''    ''']
"""
This is a
multi-line comment or docstring.
"""

'''This is a
multi-line comment or 

       docstring'''

