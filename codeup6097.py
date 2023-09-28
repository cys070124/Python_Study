w,h=map(int,input().split())
a=[[0 for j in range(h)] for i in range(w)]
n=int(input())
for i in range(n):
    l,d,x,y=map(int,input().split())
    for j in range(l):
        if d==0:
            a[x-1][y+j-1]=1
        else:
            a[x+j-1][y-1]=1
for i in range(w):
    for j in range(h):
        print(a[i][j],end=' ')
    print()