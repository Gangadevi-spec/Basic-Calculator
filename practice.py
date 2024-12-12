print("Welcome to python calculatet")
print("1.addition")
print("2.Subration")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter 1/2/3/4 :"))
num1=int(input("Enter the first value: "))
num2=int(input("Enter the second value: "))
if choice==1:
    sum=num1+num2
    print(f"Enter the value of {num1} + {num2} is {sum} :")
elif choice==2:
    sum=num1-num2
    print(f"Enter the value of {num1} - {num2} is{sum} ")
elif choice==3:
    sum=num1*num2
    print(f"Enter the vaue of {num1} * {num2} is {sum}")
elif choice==4:
    if num2!=0:
        sum=num1/num2
        print(f"Enter the value of {num1} / {num2} is {sum}")
    else:
        print("can't divided by zero")
else:
    print("enter the invalid number")