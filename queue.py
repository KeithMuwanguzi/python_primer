from collections import deque
#implementation using lists
queue= []
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
queue.append('e')
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)

#implementing using collections.deque
queue= deque()
queue.append('f')
queue.append('g')
queue.append('h')
queue.append('j')
queue.append('k')
print(queue)
print(queue.popleft())
print(queue.popleft())

print(queue)

