class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * stack_size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.stack_size - 1

    def push(self, i):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = i
            print(self.list)
            return
        else:
            print("Stack overflow")
            return

    def pop(self):
        if not self.isEmpty():
            item = self.list[self.top]
            self.top -= 1
            print(item)
            return
        else:
            print("Stack underflow")
            return

    def peek(self):
        if not self.isEmpty():
            print(self.list[self.top])
            return
        else:
            print("Stack is empty")
            return
        
    def increase(self, i): #Stack의 길이를 늘린다
        self.stack_size+=i
        self.list += [None]*i
        print("Stack size increased successfully")
        return
    
    def decrease(self, i): #Stack의 길이를 줄인다
        if i >= self.stack_size:
            print("Error : Decrease amount is greater than stack size")
            return
        if self.stack_size-self.top-1 >= i: 
            self.stack_size -= i
            self.list = self.list[:self.stack_size]
            print("Stack size decreased successfully")
            return
        else:
            self.top=self.stack_size-i-1
            self.stack_size -= i
            self.list = self.list[:self.stack_size]
            print("Stack size decreased successfully")
            return
        
    def reset(self): #Stack을 초기화 시킨다
        self.list = [None] * self.stack_size
        self.top=-1
        print("Stack was successfully initialized")
        return
