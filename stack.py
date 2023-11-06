stack_size=5
list=[None]*stack_size
top=-1

def isEmpty():
    if top==-1:return True
    else : return False
def isFull():
    return top==stack_size-1
def push(i):
    global top
    if not isFull():
        top=top+1
        list[top]=i
        print(list)
    else:
        print("stack overflow")
        exit()
def pop():
    global top
    if not isEmpty():
        item=list[top]
        top-=1
        print(item)
    else:
        print("stack underflow")
        exit()
def peek():
    if not isEmpty():
        print(list[top])
    else:pass
