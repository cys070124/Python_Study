a=int(input())
s=0
for i in range(1,a+1):
    s+=i
for i in range(a):
    for j in range(i+1):
        print(s,end=' ')
        s-=1
    print()