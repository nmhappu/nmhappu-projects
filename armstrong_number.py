a = int(input("Enter a number to check if its an armstrong no:,"))
b = str(a)
length = len(b)
result = 0

for i in b:
    i = int(i)
    result = result + i ** length    

if result == a:
    print(a,"Is an armstrong number")
else:
    print(a,"is not an armstrong number")
