from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()
print(queue)
queue.appendleft('Max')
print(queue)
#queue
