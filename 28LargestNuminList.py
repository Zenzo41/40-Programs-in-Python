list1 = []

count = int(input("How many numbers do you wanna add? "))

for n in range(count):
    number = int(input("Enter the number: "))
    list1.append(number)
    

print("Largest number in the list is:",max(list1))