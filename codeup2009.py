a,b=map(int,input().split())
s,t=0,0
while a>=b:
    t=0
    t+=a%b
    t+=a//b
    s+=a//b
    a=t
print(s)