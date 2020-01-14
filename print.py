#!/usr/bin/env python
# coding=utf-8

# Input number one
print("Please input number one")
number1 = input()
if (False == number1.isdigit()) :
    print("Invalid number")
    exit()
    
# input operator
print("Please input operator")
operator = input()

if ( (operator is not '+') and (operator is not '-') and (operator is not '*') and (operator is not '%') ) :
    print("Invaliad operator")
    exit()

if (operator is '+') :
    choice = "case1"

if (operator is '-') :
    choice = "case2"

if (operator is '*') :
    choice = "case3"

if (operator is '%'):
    choice = "case4"

# Input number 
print("Please input number two")
number2 = input()
if (False == number2.isdigit()) :
    print("Invalid number")
    exit()

# +
def case1(a, b):
    print("a + b =",int(a) + int(b))

# - 
def case2(a, b):
    print("a - b =",int(a) - int(b))

# *
def case3(a, b):
    print("a * b =", int(a) * int(b))

# %
def case4(a, b) :
    if ( int(b) == 0 ):
        print("0 cannot be divisor")
        exit()
    print("a % b = ", int(a) % int(b))

switch = {
    'case1': case1,
    'case2': case2,
    'case3': case3,
    'case4': case4
}

# Execution operation
switch.get(choice, case2)(number1, number2)
 27 
 28 if (operator is '%'):
 29     choice = "case4"
 30 
 31 # Input number 
 32 print("Please input number two")
 33 number2 = input()
 34 if (False == number2.isdigit()) :
 35     print("Invalid number")
 36     exit()
 37 
 38 # +
 39 def case1(a, b):
 40     print("a + b =",int(a) + int(b))
 41 
 42 # - 
 43 def case2(a, b):
 44     print("a - b =",int(a) - int(b))
 45 
 46 # *
 47 def case3(a, b):
 48     print("a * b =", int(a) * int(b))
 49 
 50 # %
 51 def case4(a, b) :
 52     if ( int(b) == 0 ):
 53         print("0 cannot be divisor")
 54         exit()
 55     print("a % b = ", int(a) % int(b))
 56 
 57 switch = {
 58     'case1': case1,
 59     'case2': case2,
 60     'case3': case3,
 61     'case4': case4
 62 }
 63 
 64 # Execution operation
 65 switch.get(choice, case2)(number1, number2)
 66 #print('\033[1;46m123\033[0m');      #print('\033[1;46m123\033[0m');
