class MyQueue:

    def __init__(self):
        self.queue = []
        self.start = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        peek = self.peek()  
        self.start += 1
        return  peek

    def peek(self) -> int:
        return self.queue[self.start]

    def empty(self) -> bool:
        return len(self.queue) == self.start
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()