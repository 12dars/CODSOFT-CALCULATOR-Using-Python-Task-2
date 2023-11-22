# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:02:19 2023

1@author: darshan
"""

def add(l, g):
    return l + g

def subtract(l, g):
    return l - g 

def multiply(l, g):
    return l * g  

def divide(l, g):
    if g == 0:
         return 'invalid'
    else:
        return l/ g

print("Select choice:")
print("1. Add") 
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
     choice= input("Enter the choice you want to perform: ")
     if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
     else:
        print("Invalid input")