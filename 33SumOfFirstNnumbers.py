n = int(input("Enter the value of N: "))

hold = n
sum = 0 

if(n <= 0):
    print("Enter the positive value of N which is > 0")
else:
    while n > 0:
        sum = sum + n
        n = n - 1
        

print("The sum of first ",hold," numbers is: ",sum)    
