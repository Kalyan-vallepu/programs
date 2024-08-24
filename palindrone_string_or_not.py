str=input("Enter a string:")
reverse=""
for i in reversed(str):
    reverse+=i
print(reverse)
if str==reverse:
    print(str,"is palindrome")
else:
    print(str, "is not palindrome")
