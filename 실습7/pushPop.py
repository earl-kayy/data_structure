from listQueue import *

#2개의 큐를 사용하여 push(), pop() 알고리즘 작성

class stack_2queue:
    def __init__(self):
        self.main_que = ListQueue()
        self.sub_que = ListQueue()
    
    def push(self, x):
        self.sub_que.enqueue(x)

        while not self.main_que.isEmpty():
            self.sub_que.enqueue(self.main_que.dequeue())
        
        self.main_que, self.sub_que = self.sub_que, self.main_que
    
    def pop(self):
        return self.main_que.dequeue()

stack_sim = stack_2queue()

stack_sim.push(7)
stack_sim.push(2)
stack_sim.push(3)
stack_sim.push(5)

print(stack_sim.pop())