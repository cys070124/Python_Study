def func(n):
    if n==0: return
    func(n-1)
    print("*"*n)

n=int(input())
func(n)