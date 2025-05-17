class Stack:
    def __init__(self):
        self.a = list()
    def push(self, b):
        self.a.append(b)
    def pop(self):
        self.a.pop()
    def top(self):
        if len(self.a) == 0:
            return None
        else:
            return self.a[-1]

while True:
    a = input()
    stack = Stack()
    if a == '.':
        break
    else:
        for i in range(len(a)):
            if a[i] == '(':
                stack.push('(')
            elif a[i] == ')':
                if stack.top() == '(':
                    stack.pop()
                else:
                    print('no')
                    break
            elif a[i] == '[':
                stack.push('[')
            elif a[i] == ']':
                if stack.top() == '[':
                    stack.pop()
                else:
                    print('no')
                    break
            if i == (len(a)-1) and stack.top() is None:
                print('yes')
            elif i == (len(a)-1):
                print('no')