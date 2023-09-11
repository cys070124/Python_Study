n=[[0 for j in range(20)] for i in range(20)]
a=int(input())
for i in range(a):
    x,y=map(int,input().split())
    n[x][y]=1
for i in range(1,20):
    for j in range(1,20):
        print(n[i][j],end=' ')
    print()
