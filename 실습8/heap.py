class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []

    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    # 아래에서 위까지 올라가기
    def __percolateUp(self, i:int):
        parent = (i-1)//2
        # i 가 0이면 비교할 부모가 없으므로 if 문 들어갈 필요 없고, 만약 자식(i)이 부모보다 크면 교체해서 올라가야됨
        if i>0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            # 더 올라갈 수 있으면 더 올라가야됨
            self.__percolateUp(parent)

    def deleteMax(self):
        if (not self.isEmpty()):
            # 가장 큰 값(맨 앞에 값) max 값으로 설정
            max = self.__A[0]
            # 맨 앞에를 맨 밑에 있던 애로 바꿈
            self.__A[0] = self.__A.pop()
            # 바꾼 맨 앞의 노드를 위에서 아래로 쭉 내려가게 함(자기한테 맞는 자리에 도착할 때까지) => 재정렬하는 과정 (max heap 의 구조를 유지하기 위함)
            self.__percolateDown(0)
            return max
        else:
            return None
        
    # 위에서 아래로 내려가기
    def __percolateDown(self, i:int):
        child = 2*i + 1 # 왼쪽 자식 인덱스
        right = 2*i + 2 # 오른쪽 자식 인덱스
        # child 중 인덱스가 작은 애가 범위 안에 들어가는지 확인 -> 범위 안에 안들어가면 i 는 자식이 없는 것임 -> 내려갈 곳 X, 바로 반환
        if(child <= len(self.__A)-1): 
            # 오른쪽 자식이 존재하는지(왼쪽 자식만 있을수도) 확인 -> and 이전 조건
            # 두 자식 중 더 큰 자식만 선정(더 큰 자식보다 작으면 부모가 내려가야됨) -> and 이후 조건 (2개 비교해서 큰 자식 선정)
            if(right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
                child = right
            # 자식들 중 더 큰 애랑 비교해서 걔 보다 작으면 교체 (자식이 올라가야됨 - 가장 큰 애가 위에 있어야 하니까)
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                # 더 내려갈 수 있으면 더 내려가야됨
                self.__percolateDown(child)

    def max(self):
        return self.__A[0]

    # 리스트가 주어졌을 때 주어진 리스트를 max heap 의 형태로 정렬하는 과정
    def buildHeap(self):
        for i in range((len(self.__A)-2)//2, -1, -1):
            self.__percolateDown(i)
    
    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A = []

    def size(self) -> int:
        return len(self.__A)

    def heapPrint(self):
        print("============================")
        n = 1
        for i in range(self.size()):
            print(self.__A[i], end = ' ')
            if(i == 2**n-2):
                print()
                n += 1
        print()