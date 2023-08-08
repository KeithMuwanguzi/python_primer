# importing "heapq" to implement heap queue
import heapq

li = [6, 8, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)
print(list(li))

#appending elements to a heap
heapq.heappush(li, 4)
print(list(li))
#popping elemet from heap
heapq.heappop(li)
print(list(li))
print(heapq.heappop(li))

