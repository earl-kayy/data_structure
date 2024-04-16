from lpnFreq import *

# LFU 캐시의 구현 (가장 freq 작은 객체가 맨 위 자리에 위치)
class MinHeap:
    def __init__(self):
            # heap 의 내부 각 요소는 LpnFreq 의 객체로 구성
            self.__heap = []
       
    def insert(self, lpnfreq):
        self.__heap.append(lpnfreq)
        self.__percolateUp(len(self.__heap)-1)

    # 아래에서 위까지 올라가기 -> 부모보다 작은 자식이 올라가는 과정
    def __percolateUp(self, i:int):
        parent = (i-1)//2
        # i 가 0이면 더 이상 비교할 부모가 없으므로 if 문 지나쳐도 되고, 자식(i)이 부모(parent)보다 작을 경우 교체해야함
        if i>0 and self.__heap[i] < self.__heap[parent]:
            self.__heap[i], self.__heap[parent] = self.__heap[parent], self.__heap[i]
            # 더 올라갈 수 있으면 올라가야됨
            self.__percolateUp(parent)

    # evict 되면서 storage 에 상태 저장해야됨
    def deleteMin(self):
        if (not self.isEmpty()):
            # 가장 작은 lpnfreq 객체를 min 값에 넣음
            min = self.__heap[0]
            # 기존 맨 앞자리(가장 작은애가 와야되는 자리)에 맨 뒤에 있던 애를 넣어줌
            self.__heap[0] = self.__heap.pop()
            # 바뀐 맨 앞에 오는 애를 자기한테 맞는 자리에 올 때까지 천천히 내려보냄
            self.__percolateDown(0)
            return min
        else:
            return None
        
    # 위에서 아래로 내려가기 -> 자식보다 큰 부모가 내려가는 과정
    def __percolateDown(self, i:int):
        child = 2*i + 1 # 왼쪽 자식 인덱스
        right = 2*i + 2 # 오른쪽 자식 인덱스
        # child 중 인덱스가 작은 애가 범위 안에 들어가는지 확인 -> 범위 안에 안들어가면 i 는 자식이 없는 것임 -> 내려갈 곳 X, 바로 반환
        if(child <= len(self.__heap)-1):
            # 오른쪽 자식이 존재하고, 오른쪽 자식이 왼쪽 자식보다 작으면, 오른쪽 자식만 비교 (어차피 작은 애보다 작으면 되니까)
            if(right <= len(self.__heap)-1 and self.__heap[child] > self.__heap[right]):
                child = right
            # 자식들 중 작은 애랑 비교해서 걔보다 크면 교체 (자식이 올라가야됨 - 가장 작은 애가 위에 있어야하니까)
            if self.__heap[i] > self.__heap[child]:
                self.__heap[i], self.__heap[child] = self.__heap[child], self.__heap[i]
                # 더 내려갈 수 있으면 더 내려가기
                self.__percolateDown(child)

    def min(self):
        return self.__heap[0]
    
    def isEmpty(self) -> bool:
        return len(self.__heap) == 0

    def clear(self):
        self.__heap = []

    def size(self) -> int:
        return len(self.__heap)

    def getHeap(self):
        return self.__heap

    def find(self, lpn):
        for i in range(self.size()):
            if self.__heap[i].getLpn() == lpn:
                return (self.__heap[i], i)
        return None, None

    # heap 의 객체에 freq 갱신 후, min heap 구조 유지하기 위해 아래쪽으로 내려보낼 수 있으면 내려보내야함
    # 복잡도 최소화 위해 해당 지점을 지정해 거기서부터 정렬 시작
    def updateHeap(self, index):
        self.__percolateDown(index)