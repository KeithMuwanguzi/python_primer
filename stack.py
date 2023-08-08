from collections import deque
#implementation using lists
stack= []
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

#implementing using collections.deque
stack= deque()
stack.append('f')
stack.append('g')
stack.append('h')
stack.append('j')
stack.append('k')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

