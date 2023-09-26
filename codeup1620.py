a=input()
s=0
while len(a)>1:
    i=0
    for i in range(len(a)):
        s+=int(a[i])
    a=str(s)
    s=0
print(a)