# 4] Write a Python function to find the maximum of three numbers.


num1=input("Enter The Number1 : \n")
num2=input("Enter The Number2 : \n")
num3=input("Enter The Number3 : \n")
num4=input("Enter The Number4 : \n")

max=0

if (num1>num2) & (num1>num3) & (num1>num4):
    print("Num1 is Greater \n")
    max=num1

elif  (num2>num3) & (num2>num4):
    print("Num2 is Greater \n")
    max=num2

elif num3>num4:
    print("Num3 is Greater \n")
    max=num3


print(f"Max Number Is = {max}")

