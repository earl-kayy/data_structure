from list.listNode import ListNode

class CircularLinkedList:
    """원형 연결 리스트 클래스"""
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0
    
    def insert(self, i: int, newItem) -> None: #i번째 위치에 item 추간
        if (i >= 0 and i <= self.__numItems):
            # 0 <= i < self.__numItems => '삽입'
            # i == self.__numItems => '마지막에 추가
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next) # 새 노드는 i+1 번 노드를 가리켜야함
            prev.next = newNode # i-1 번 노드는 새로 추가된 노드를 가리켜야함
            if i == self.__numItems: # 마지막에 추가하는 경우
                self.__tail = prev.next
            self.__numItems += 1
        else:
            raise IndexError("리스트 범위를 벗어난 인덱스입니다.")

    def append(self, newItem) -> None: # list 끝에 새 항목 추가
        self.insert(self.__numItems, newItem)

    def pop(self, *args): # pop(), pop(-1) : 마지막 원소 pop + pop(i): i 번째 원소 pop
        # list 에 아무것도 없을 경우
        if self.isEmpty():
            return None
        # 일반적인 경우 처리
        if len(args) != 0:
            index = args[0]
        if index == -1 or len(args) == 0: #pop(-1), pop() 의 경우
            index = self.__numItems-1
        if (0<=index and index<self.__numItmes): # 리스트 범위 안에 잘 있을 경우
            prev = self.getNode(index-1)
            popItem = prev.next.item
            prev.next = prev.next.next # pop 이전 요소가 pop 된 애의 다음 요소를 가리키게함
            if(index == self.__numItems-1): # 마지막 요소 pop 시, tail 이전껄로 바뀜
                self.__tail = prev
            self.__numItems -= 1
            return popItem
        else:
            raise IndexError("리스트 범위를 벗어난 인덱스입니다.")

    def remove(self, x): # x 라는 item 을 갖는 애 삭제
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail: #마지막 요소를 삭제할 경우 tail 재설정 해줘야함
                self.__tail = prev
            self.__numItems -= 1
        else:
            return None

    def get(self, *args): #pop 과 유사하지만 삭제하지 않고 item 만 리턴해줌
        if self.isEmpty():
            return None
        if len(args) != 0: #실제 입력된게 있다면
            index = args[0]
        if (len(args) == 0 or index == -1): # 실제 입력된게 없거나 index 가 0일 경우
            index = self.__numItems - 1
        if(index >= 0 and index < self.__numItems):
            return self.getNode(index).item
        else:
            return None

    def index(self, x) -> int: # x item 을 가지는 노드의 index
        index = 0
        for element in self:
            if element == x:
                return index
            index += 1
        return -777

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self): 
        # 기존에 있던 dummy 노드를 사용하는게 아니라 다 갖다 버리고 새로 dummy 생성한다는 느낌
        # 리스트 갈아치울 땐 더미도 새로 만들어버림
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def count(self, x) -> int:
        count = 0
        for element in self:
            if element == x:
                count += 1
        return count

    def extend(self, a):
        for item in a:
            self.append(item)

    def copy(self) -> b'CircularLinkedList':
        new_list = CircularLinkedList()
        for element in self:
            new_list.append(element)
        return new_list

    def reverse(self) -> None:
        __head = self.__tail.next # dummy
        prev = __head #dummy
        curr = prev.next #0번째 요소
        next = curr.next #1번째 요소
        # 0번째 요소 -> 더미 가리키게 (마지막 요소가 됨)
        curr.next = __head
        # 더미 -> 기존 마지막 요소 가리키게 (맨 첫번째 요소가 됨)
        __head.next = self.__tail
        # 기존 첫번째 요소가 tail 됨
        self.__tail = curr
        # 한칸씩 오른쪽으로 옮기고 재정렬(포인팅 새로 할 수 있게)
        for i in range(self.__numItems - 1):
            prev = curr
            curr = next
            next = next.next
            # 새로 가리키기
            curr.next = prev

    def sort(self) -> None:
        tmp = []
        for element in self:
            tmp.append(element)
        tmp.sort()
        self.clear()
        for element in tmp:
            self.append(element)

    def __findNode(self, x) -> (ListNode, ListNode):
        __head = prev = self.__tail.next #dummy
        curr = prev.next #0번째 요소
        while curr != __head:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
        return (None, None)

    def getNode(self, i: int) -> ListNode:
        curr = self.__tail.next # dummy
        for index in range(i+1):
            curr = curr.next
        return curr

    def printList(self) -> None:
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1) #dummy
        self.iterPosition = self.__head.next #0번째 요소

    def __next__(self):
        if self.iterPosition == self.__head: #dummy 까지 도달 = 마지막까지 다 돌았다는 뜻
            raise StopIteration
        else: # 현재 요소 리턴 + 다음 요소로 포지션 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item