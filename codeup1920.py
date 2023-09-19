def func(a):
    if a>1: func(a//2)
    print(a%2,end='')
a=int(input())
func(a)