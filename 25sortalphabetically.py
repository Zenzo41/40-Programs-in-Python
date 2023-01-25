stringvalue = input("Enter your string:")

values_after_split = stringvalue.split()

values_after_split.sort()

for word in values_after_split:
    print(word)