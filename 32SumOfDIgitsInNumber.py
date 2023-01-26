value = int(input("Enter your integer value: "))

num = value
sum = 0

while value > 0:
    rem = value % 10
    sum = sum + rem
    value = int(value / 10)
    

print("Sum of the value",num," is:",sum)