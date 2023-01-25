punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

stringval = input("Enter your string value:")

no_punctuation=''
for char in stringval:
     if char not in punctuations:
        no_punctuation += char
        
print(no_punctuation)