#SIMPLE CALCULATOR
#This script performs +, -, * or / of 2 given numbers 

#Returns the sum of num1 and num2
def add(num1, num2):
    return num1 + num2
#Returns the substration of num1 and num2
def sub(num1, num2):
    return num1 - num2
#Returns the product of num1 and num2
def mult(num1, num2):
    return num1 * num2
#Returns the division of num1 by num 2
def div(num1, num2):
    return num1 / num2

def main():
    operation = input ("What do you want to do (+, -, *, /): ")
    while (operation !="+" and operation != "-" and operation != "*" and operation != "/"):
        print (operation," is not a valid opreator")
        operation = input ("Please select one among these (+, -, *, /): ")
    else:
        flag=0
        while flag==0:
            var1=input("Enter num 1: ")
            try:
                float(var1)
                flag=1
            except ValueError:
                print(var1,"is not a number.")
                flag=0
                
        var1=float(var1)
        var2=input("Enter num 2: ")
        flag=0
        while flag==0:
            try:
                float(var2)
                flag=1
            except ValueError:
                print(var2,"is not a number.")
                flag=0
        var2=float(var2)
        if (operation == "+"):
            print(add(var1, var2))
        elif (operation == "-"):
            print(sub(var1, var2))
        elif (operation == "*"):
            print(mult(var1, var2))
        else:
            if var2==0:
                print("Division cannot be performed with divider 0")
                return
            print(div(var1, var2))
main()
