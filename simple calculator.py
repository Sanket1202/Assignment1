def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

while True:
 
    print("1.addition\n","2.subtraction\n","3.multiplication\n","4.division\n")
    choice  = int(input("enter your choice:"))
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    if choice == 1:
        print(add(num1,num2))
    elif choice == 2:
        print(sub(num1,num2))
    elif choice == 3:
        print(mul(num1,num2))
    elif choice == 4:
        print(div(num1,num2))
    else:
        print("enter valid number")
    