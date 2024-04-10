class MinHeap: # lpn 하나, dict 하나
    def __init__(self, cache_slots):
            self.lpn = [cache_slots]
            # freq 를 lpn 이 바뀔 때마다 바꿀 수 없으므로
            # self.freq = {}

    def insert(self, x):
        self.lpn.append(x)
        self.__percolateUp(len(self.lpn)-1)

    # 아래에서 위까지 올라가기 -> 부모보다 작은 자식이 올라가는 과정
    def __percolateUp(self, i:int):
        parent = (i-1)//2
        # i 가 0이면 더 이상 비교할 부모가 없으므로 if 문 지나쳐도 되고, 자식(i)이 부모(parent)보다 작을 경우 교체해야함
        if i>0 and self.lpn[i] < self.lpn[parent]:
            self.lpn[i], self.lpn[parent] = self.lpn[parent], self.lpn[i]
            # 더 올라갈 수 있으면 올라가야됨
            self.__percolateUp(parent)

    def deleteMin(self):
        if (not self.isEmpty()):
            # 가장 작은 값을 min 값에 넣음
            min = self.lpn[0]
            # 기존 맨 앞자리(가장 작은애가 와야되는 자리)에 맨 뒤에 있던 애를 넣어줌
            self.lpn[0] = self.lpn.pop()
            # 바뀐 맨 앞에 오는 애를 자기한테 맞는 자리에 올 때까지 천천히 내려보냄 => 일종의 재정렬(min lpn 의 구조를 유지하기 위함)
            self.__percolateDown(0)
            return min
        else:
            return None
        
    # 위에서 아래로 내려가기 -> 자식보다 큰 부모가 내려가는 과정
    def __percolateDown(self, i:int):
        child = 2*i + 1 # 왼쪽 자식 인덱스
        right = 2*i + 2 # 오른쪽 자식 인덱스
        # child 중 인덱스가 작은 애가 범위 안에 들어가는지 확인 -> 범위 안에 안들어가면 i 는 자식이 없는 것임 -> 내려갈 곳 X, 바로 반환
        if(child <= len(self.lpn)-1):
            # 오른쪽 자식이 존재하고, 오른쪽 자식이 왼쪽 자식보다 작으면, 오른쪽 자식만 비교 (어차피 작은 애보다 작으면 되니까)
            if(right <= len(self.lpn)-1 and self.lpn[child] > self.lpn[right]):
                child = right
            # 자식들 중 작은 애랑 비교해서 걔보다 크면 교체 (자식이 올라가야됨 - 가장 작은 애가 위에 있어야하니까)
            if self.lpn[i] > self.lpn[child]:
                self.lpn[i], self.lpn[child] = self.lpn[child], self.lpn[i]
                # 더 내려갈 수 있으면 더 내려가기
                self.__percolateDown(child)

    def min(self):
        return self.lpn[0]
    
    def isEmpty(self) -> bool:
        return len(self.lpn) == 0

    def clear(self):
        self.lpn = []

    def size(self) -> int:
        return len(self.lpn)