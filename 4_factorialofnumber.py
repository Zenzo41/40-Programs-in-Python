def functionforfactorial(num):
    if num == 1:
        return num
    else:
        return num * functionforfactorial(num-1)
    
num = int(input("Enter the number to find the factorial:"))

if num < 0:
    print("The factorial of the given number can not be found")
elif num == 1:
     print("The factorial of 0 is 1")
else:
    print("The factorial of the given number is :",functionforfactorial(num))