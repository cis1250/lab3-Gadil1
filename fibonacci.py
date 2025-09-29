#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
n = input("Enter the number of terms: ")
# Validate that the input is a positive integer.
while not n.isdigit() or int(n) <= 0:
  print ("Please enter a positive integer.")
  n = input("Enter the number of terms: ")

  n = int(n)
  a = 0
  b = 1
# Use a for loop to print the Fibonacci sequence up to that many terms.


for x in range(n):
print(a, end=" ")
a, b = b, a + b
