# lpn, frequency 관리하는 클래스
class LpnFreq:
    def __init__(self, lpn, freq):
        self.lpn = lpn
        self.freq = freq
    
    # LpnFreq 의 객체 A, B 가 있고, 2 객체가 각각 heap[0], heap[1] 안에 들어가 있을 때, heap[0], heap[1] 을 비교한다고 가정
    # heap[0], heap[1] 는 각각 객체이므로 서로 비교할 수가 없음
    # 따라서 '<' 를 오버로딩해서 객체간의 비교는 곧 객체 안의 freq 변수의 크기비교라고 재정의
    # 추후, '<' 연산자 앞뒤로 객체가 오면 아래 정의된 방식으로 연산됨
    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __eq__(self, other):
        return self.lpn == other.lpn

    def getLpn(self):
        return self.lpn

    def getFreq(self):
        return self.freq

    # 한번 참조될 때마다 frequency 값 하나 더해줌
    def addFreq(self):
        self.freq += 1