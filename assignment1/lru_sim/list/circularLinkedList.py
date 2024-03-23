from list.listNode import ListNode

class CircularLinkedList:
    """원형 연결 리스트 클래스"""
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0
    
    def insert(self, i: int, newItem):
        """리스트의 i번째 위치에 새 항목을 삽입"""
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i-1) if i > 0 else self.__tail
            prev.next = ListNode(newItem, prev.next)
            if i == self.__numItems:
                self.__tail = prev.next
            self.__numItems += 1
        else:
            raise IndexError("리스트 범위를 벗어난 인덱스입니다.")

    def append(self, newItem):
        """리스트의 끝에 새 항목을 추가"""
        self.insert(self.__numItems, newItem)

    def pop(self, index=None):
        """리스트의 특정 위치의 항목을 제거하고 반환"""
        if self.__numItems == 0:
            raise IndexError("비어 있는 리스트에서는 제거할 수 없습니다.")

        if index is None or index == self.__numItems - 1:
            index = self.__numItems - 1  # 마지막 항목 제거

        if not (-self.__numItems <= index < self.__numItems):
            raise IndexError("리스트 범위를 벗어난 인덱스입니다.")

        if index < 0:
            index += self.__numItems  # 음수 인덱스 처리

        prev = self.getNode(index - 1)
        remove = prev.next
        prev.next = remove.next  # 제거할 노드를 건너뛰고 연결

        if index == self.__numItems - 1:  # 마지막 항목을 제거하는 경우
            self.__tail = prev  # tail 업데이트

        self.__numItems -= 1
        return remove.item


    def remove(self, x):
        """리스트에서 x와 같은 첫 번째 항목을 제거"""
        prev, node = self.__findNode(x)
        if node:
            prev.next = node.next
            if node == self.__tail:
                self.__tail = prev
            self.__numItems -= 1
        else:
            raise ValueError(f"{x}는 리스트에 없습니다.")

    def get(self, i: int):
        """리스트의 i번째 항목을 반환"""
        if not (0 <= i < self.__numItems):
            raise IndexError("리스트 범위를 벗어난 인덱스입니다.")
        return self.getNode(i).data

    def index(self, x) -> int:
        """리스트에서 x와 같은 첫 번째 항목의 위치를 반환. 없으면 -1을 반환"""
        curr = self.__tail.next
        for index in range(self.__numItems):
            if curr.data == x:
                return index
            curr = curr.next
        return -1

    def isEmpty(self) -> bool:
        """리스트가 비어있는지 확인"""
        return self.__numItems == 0

    def size(self) -> int:
        """리스트의 크기를 반환"""
        return self.__numItems

    def clear(self):
        """리스트의 모든 항목을 제거"""
        self.__tail.next = self.__tail
        self.__numItems = 0

    def count(self, x) -> int:
        """리스트에서 x와 같은 항목의 수를 반환"""
        count = 0
        curr = self.__tail.next
        for _ in range(self.__numItems):
            if curr.data == x:
                count += 1
            curr = curr.next
        return count

    def extend(self, a):
        """다른 리스트 a의 항목들을 현재 리스트의 끝에 추가"""
        for item in a:
            self.append(item)

    def copy(self):
        """리스트의 복사본을 반환"""
        new_list = CircularLinkedList()
        curr = self.__tail.next
        for _ in range(self.__numItems):
            new_list.append(curr.data)
            curr = curr.next
        return new_list

    def reverse(self) -> None:
        """리스트의 항목들을 역순으로 배치"""
        prev = self.__tail
        curr = self.__tail.next
        for _ in range(self.__numItems):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.__tail.next.next = self.__tail
        self.__tail = self.__tail.next

    def sort(self) -> None:
        """리스트를 오름차순으로 정렬"""
        # 간단한 삽입 정렬로 구현될 수 있지만, 원형 연결 리스트에는 비효율적일 수 있습니다.
        # 효율적인 정렬 알고리즘을 사용하는 것이 좋습니다.

    def __findNode(self, x) -> (ListNode, ListNode):
        """x 값을 갖는 노드와 그 이전 노드를 찾아서 반환"""
        prev = self.__tail
        curr = self.__tail.next
        while curr != self.__tail:
            if curr.data == x:
                return prev, curr
            prev = curr
            curr = curr.next
        return None, None

    def getNode(self, i: int) -> ListNode:
        """i번째 노드를 반환"""
        curr = self.__tail.next
        for _ in range(i + 1):
            curr = curr.next
        return curr

    def printList(self) -> None:
        """리스트의 모든 항목을 출력"""
        curr = self.__tail.next
        for _ in range(self.__numItems):
            print(curr.data, end=" -> ")
            curr = curr.next
        print("리스트의 끝")

    def __iter__(self):
        """리스트의 이터레이터를 반환"""
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    """원형 연결 리스트의 이터레이터 클래스"""
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item