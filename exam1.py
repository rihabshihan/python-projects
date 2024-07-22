# 1. Write a program to print N rows in the following pattern

# **

# ***

n=int(input("Enter the number"))
for i in range(n):
   for j in range(i+1):
      print("*", end="")
   print()
   