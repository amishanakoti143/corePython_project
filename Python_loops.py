# Python_Loops.py
"""
Topic: Loops in Python
Author: Amisha Nakoti
"""

# ---------------------------
# What are Loops?
# ---------------------------
# Loops are used to execute a block of code repeatedly.
# Python supports two main types of loops:
# 1. for loop
# 2. while loop

# ---------------------------
# for Loop
# ---------------------------
# Used to iterate over a sequence (like list, string, range, etc.)

print("Using for loop with range:")
for i in range(5):
    print("Value:", i)

print("\nUsing for loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ---------------------------
# while Loop
# ---------------------------
# Executes as long as the condition is true

print("\nUsing while loop:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

'''___________________FOR_loop__________|🆚|_____________WHILE_loop______________________'''

#   ● Work with sequence or range.             ● work with condition
#   ● loop control is built-in like-           ● You must manually update condition
#     range(start,end,step)  
#   ● when you know how many times to repeat.  ● when you don't know how many times to repeat.

#   ● When you looping overime (fixed range).  ●  loop until a condition become false.


# ---------------------------
# break Statement
# ---------------------------
# Used to exit the loop prematurely

print("\nUsing break in a loop:")
for i in range(10):
    if i == 5:
        break
    print("Break Example:", i)

# ---------------------------
# continue Statement
# ---------------------------
# Skips the current iteration and moves to the next

print("\nUsing continue in a loop:")
for i in range(5):
    if i == 2:
        continue
    print("Continue Example:", i)

# ---------------------------
# Nested Loops
# ---------------------------
# Loops within loops

print("\nNested loop output:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)

# ---------------------------
# else with Loops
# ---------------------------
# The else block executes after the loop ends normally (no break)

print("\nUsing else with for loop:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Loop_Questions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''print counting 1 to 10'''
x=1
while x<=10:       #by while loop
    print(x)
    x+=1

#--------------------------------------
for i in range(1,11 ):    # for loop
    print(i)

'''Print "hello World" ten times by for and while loop '''
x=1
while x<=10:
    print("helloword")
    x+=1
#----------------------
for i in range(1,11):
    print("Hello World")

'''print counting from 10 to 20 by for and while loop'''
x=10
while x<=20:
    print(x)
    x+=1
#-------
for i in range(10,21):
    print(i)


'''backword counting 20 to 1 by while and for loop'''
x=20
while x>=1:
    print(x,end="|")
    x-=1

#-----------
for i in range(20,0,-1):
    print(i)

#---------------------------------------------------
# print all even number 1 to 20 by for and while.
x=1
while x<=20:
    if x%2==0:
        print(x) 
    x+=1
#--------------------
for i in range(1,21):
    if i%2==0:
        print("Even no : ",i)

# print all odd number 1 to 20 by for and while.
x=1
while x<=20:
    if x%2!=0:
        print(x) 
    x+=1

#--------------
for i in range(1,21):
    if i%2!=0:
        print("Odd no : ",i)

#to print all number which is divisible by 3 and 2 

for i in range (10,41):
    if i%3==0 and i%2==0:
        print(i)


#count all even number from 10 to 25

c=0
for i in range (10,26):
    if i%2==0:
        c+=1
print(c)







