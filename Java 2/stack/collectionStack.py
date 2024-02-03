import collections

stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.pop()
print(stack)
print(stack[-1]) #checking whether it is empty