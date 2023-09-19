def func(a):
    if a==1:
        return 1
    return a * func(a-1)
a=int(input())
print(func(a))