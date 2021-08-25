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