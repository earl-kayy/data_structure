from listQueue import ListQueue
import threading
import time

class Producer:
    def __init__(self, items, normal, gold, platinum):
        self.__alive = True
        self.items = items
        self.normal = normal
        self.gold = gold
        self.platinum = platinum
        self.pos = 0
        self.worker = threading.Thread(target = self.run)

    def get_item(self):
        if self.pos < len(self.items):
            item = self.items[self.pos]
            self.pos += 1
            return item
        else:
            return None

    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item = self.get_item()
                if item == None:
                    print("Arrived:", item)
                elif item[0] == '1':
                    self.normal.enqueue(item[1])
                    print("Arrived:", item[1], "(Normal)")
                elif item[0] == '2':
                    self.gold.enqueue(item[1])
                    print("Arrived:", item[1], "(Gold)")
                else :
                    self.platinum.enqueue(item[1])
                    print("Arrived:", item[1], "(Platinum)")
            else:
                break

        print("Producer is dying...")

    def start(self):
        self.worker.start() # thread 시작하는 코드
        # 이 코드 시작하고 나서부터 가서 줄서고 있음

    def finish(self):
        self.__alive = False # 위의 thread 가 더이상 run 하지 않을 수 있음(죽을 준비 함)
        self.worker.join()

class Consumer:
    def __init__(self, normal, gold, platinum):
        self.__alive = True
        self.normal = normal
        self.gold = gold
        self.platinum = platinum
        self.worker = threading.Thread(target=self.run)

    def run(self):
        while True:
            time.sleep(1)
            if self.__alive:
                if not self.platinum.isEmpty():
                    print("Boarding:", self.platinum.dequeue(), "(Platinum)")
                elif not self.gold.isEmpty():
                    print("Boarding:", self.gold.dequeue(), "(Gold)")
                elif not self.normal.isEmpty():
                    print("Boarding:", self.normal.dequeue(), "(Normal)")
            else:
                break
        print("Consumer is dying.")

    def start(self):
        self.worker.start() # thread 시작하는 코드(Thread 모듈 내)
        # 이 코드 실행시키고 나서부터 CPU 가서 줄 서고 있음

    def finish(self):
        self.__alive = False # 위의 thread 가 더이상 run 하지 않을 수 있음(죽을 준비 함)
        self.worker.join() # 위의 False 신호를 보내놓고, 프로세스가 죽었는지 프로세스의 시체를 확인하는 과정

if __name__ == "__main__":
    
    customers = []
    with open("customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # Priority - 3번

    # 등급 별 큐 생성
    normal = ListQueue()
    gold = ListQueue()
    platinum = ListQueue()
    
    producer = Producer(customers, normal, gold, platinum)
    consumer = Consumer(normal, gold, platinum)
##############################################
    # consumer = Consumer()    
    producer.start()
    consumer.start()
    time.sleep(10)
    producer.finish()
    consumer.finish()
