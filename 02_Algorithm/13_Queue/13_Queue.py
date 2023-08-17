# def enQ(data):
#     global rear
#     if rear == Qsize - 1:
#         print('Q is Full')
#
#     else:
#         rear += 1
#         Q[rear] = data
#
# def deQ():
#     global front
#     if front == rear: # 비어있으면
#         print('큐가 비어있음')
#         return
#     front += 1
#     return Q[front]
#
# while front != rear:
#     front += 1
#     print(Q[front])
#
#
# Qsize = 3
# Q = [0] * 3
# rear = -1
# front = -1
# enQ(1)
# enQ(2)
# enQ(3)
# enQ(4)
# deQ()
# deQ()
# deQ()
# deQ()

# # 원형 큐 --
def enq(data):
    global rear, front
    if (rear + 1) % cQsize == front:
        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data

def deq():
    global front
    front = (front + 1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

# enq(1)
# enq(2)
# enq(3)
# enq(4)
# enq(5)
# print(deq())
# print(deq())
# print(deq())
# print(deq())

# 마이쮸
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())
print(q.popleft())
print(q.popleft())