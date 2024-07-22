# 2. Write a program to enter a number and print its multiplication table till 10 rows.

num1=int(input("enter the number"))
for i in range(1,11):
    result= i*num1
    print("{} * {} = {}".format(i,num1,result))