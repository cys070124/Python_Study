n=int(input())
c=0
a=[]
a = list(map(int,input().split()))
b=sorted(a,reverse=True)
for i in range(n):
    for j in range(n):
        if a[i]==b[j]:
            if c==0:
                print(a[i],j+1,end=' ')
            c+=1
    print()
    c=0