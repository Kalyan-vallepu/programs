a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b=[]
c=[]
vowel="aeiouAEIOU"
for i in a:
    if i in vowel:
        c.append(i)
    else:
        b.append(i)
print("the list is:",a)
print("list without vowel:",b)
print("the removed letters:",c)