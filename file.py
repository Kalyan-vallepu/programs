A=open("sample1.txt","r")
B=A.read()
C=B.split()
for i in range(len(C)):
    if C[i]=="file":
        C[i]="Nofile"
print(C)
print(" ".join(C)) 

  	
	