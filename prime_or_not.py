n=int(input("enter the number: "))
count=0
for i in range(1,n+1):
        if n%i==0:
            count+=1
print(count)
if count==2:
    print(i,"is prime number")
else:
    print(i,"is not a prime number")