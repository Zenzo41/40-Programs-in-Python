num1 = int(input("Enter the value for num1: "))
num2 = int(input("Enter the value for num2: "))
num3 = int(input("Enter the value for num3: "))

if(num1 > num2 and num1 > num3):
    print(f'{num1} is largest among the three')
elif(num2 > num1 and num2 > num3):
    print(f'{num2} is largest among the three')
else:
     print(f'{num3} is largest among the three')