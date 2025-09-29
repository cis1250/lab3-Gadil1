#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.

# Ask for input
n = input("Enter the number of terms: ")

# Validate until it's a positive integer
while not n.isdigit() or int(n) <= 0:
    print("Please enter a positive integer.")
    n = input("Enter the number of terms: ")

# Convert to int AFTER validation
n = int(n)

# Fibonacci sequence
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
