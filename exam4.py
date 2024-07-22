# 4. Create a calculator program using OOPS. Make sure you create a class Calculator and then use its object 
# to access the calculator operations such as addition, subtraction, division and multiplication.

class calculator:
    
    def addition(self,num1,num2):
        result= num1 + num2
        return result
    
    def substract(self,num1,num2):
        result=num1-num2
        return result  
    
    def division(self,num1,num2):
        if num2==0:
            print("cannot divide by zero")
        else:
            result=num1 / num2
            return result
        
    def multiplication(self,num1,num2):
        result=num1 * num2
        return result
    
calc = calculator()
    
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
operation= input("Enter the operation(+,-,*,/)")

if operation== '+':
    result=calc.addition(num1,num2)
elif operation=='-':
    result=calc.substract(num1,num2)
elif operation=='*' :
    result=calc.multiplication(num1,num2)
elif operation=='/':
    res=calc.division(num1,num2)
else:
    print(" invalid  operation")
    
    
print("Result: ",res)