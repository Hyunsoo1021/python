class Stack:
    def __init__(self):
        self.list = []

    def push(self, a):
        self.list.append(a)

    def pop(self):
        self.list.pop()

    def top(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0

    def print(self):
        print(self.list)

num = int(input())
for i in range(num):
    a = input()
    stack1 = Stack()
    end = True
    for j in range(len(a)):
        if a[j] == '(':
            stack1.push('(')
        else:
            if not stack1.is_empty():
                stack1.pop()
            else:
                end = False
                break
    if end and stack1.is_empty():
        print('YES')
    else:
        print('NO')
