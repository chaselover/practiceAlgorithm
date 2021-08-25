from SWEA4875미로 import N


class MyQueue:
 
    def __init__(self, n):
        self.front = 0
        self.rear = 0
        self.n = n
        self.arr = [0] * self.n
 
    def my_enqueue(self, data):
        if self.my_isfull():
            print('Queue is full')
            return
 
        self.rear += 1
        self.rear %= self.n
        self.arr[self.rear] = data
 
    def my_dequeue(self):
        if self.my_isempty():
            print('Queue is empty')
            return
 
        self.front += 1
        self.front %= self.n
 
        return self.arr[self.front]
 
    def my_isempty(self):
        return self.front == self.rear
 
    def my_isfull(self):
        return (self.front - 1) % self.n == self.rear


for tc in range(1, 11):
    _ = input()
    numbers = list(map(int, input().split()))

    # 큐 생성
    queue = MyQueue(9)
    for number in numbers:
        queue.my_enqueue(number)

    # 반복
    playing = True
    while playing:
        for i in range(1, 6):
            now = queue.my_dequeue()  # 삭제
            nxt = max(now - i, 0)


class Queue:

    def __init__(self,n):
        self.front = 0
        self.rear = 0
        self.n = n
        self.arr = [0]*self.n

    def en_queue(self,data):
        if self.isfull():
            print('Queue is full')
            return
        
        self.rear += 1
        self.rear %= self.n
        self.arr[self.rear] = data
    
    def de_queue(self):
        if self.isempty():
            print('Queue is empty')
            return
        
        self.front += 1
        self.front %= self.n

        return self.arr[self.front]

    def isfull(self):
        return (self.front - 1) % self.n == self.rear
    
    def isempty(self):
        return self.front == self.rear
    
    def peek(self):
        return self.arr[self.front]