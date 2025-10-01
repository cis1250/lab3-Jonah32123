#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

userNum = input("Enter a positive integer: ")
currentNum = 0
tmp = 0
prevNum = 1

try:
  if int(userNum) > 0:
    for i in range(0,int(userNum)):
      print("{}".format(currentNum), end = " ")
      tmp = currentNum
      currentNum += prevNum
      prevNum = tmp
  else:
    print("Please enter a positive integer")
except Exception:
  print("Please enter a positive integer")
