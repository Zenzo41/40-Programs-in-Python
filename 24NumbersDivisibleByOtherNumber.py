my_list = [12, 65, 24, 39, 102, 52, 48, 36, 7, 9, 26]

result = list(filter(lambda a: (a % 2 ==0),my_list))
# filter returns those items of iterable for which function(item) is true

print("Numbers divisible by 12 are: ",result)