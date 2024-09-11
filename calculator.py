import math
def calculator():
    print("Choose the operation you want to perfrom: ")
    print("1.For Addition")
    print("2.For Subtraction")
    print("3.For Multiplication")
    print("4.For division")
    print("5.For Square root")
    print("6.For Exit")
    choice = input("Enter your choice: ")
    if choice =="1":
        n1 = float(input("Enter the first number :"))
        n2 = float(input("Enter the second number :"))
        print("The addition is:",n1+n2)
    elif choice =="2":
        n1 = float(input("Enter the first number :"))
        n2 = float(input("Enter the second number :"))
        print("The Subtraction is:",n1-n2) 
    elif choice == "3":
        n1 = float(input("Enter the first number :"))
        n2 = float(input("Enter the second number :"))
        print("The Multiplication is:",n1*n2)
    elif choice =="4":
        n1 = float(input("Enter the first number :"))
        n2 = float(input("Enter the second number :"))
        print("The Division is:",n1/n2)
    elif choice =="5":
        n = float(input("Enter the number :"))
        print("The Square root is:",math.sqrt(n))
    elif choice =="6":
        print("You choose to exit.By...")
    else :
        print("Invalid choice...")
    
calculator()