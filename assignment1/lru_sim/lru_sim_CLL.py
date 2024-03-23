class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 0
        self.cache = []

    def do_sim(self, page):
        self.tot_cnt += 1

        if page in self.cache: # hit 났을 때
            self.cache_hit += 1 #hit 횟수 추가
            self.cache.remove(page) #page 있는 자리에서 빼고
            self.cache.insert(0, page) #page MRU(맨앞)로 배치

        else: #miss 났을 때 해당 page 채워넣어야됨
            if len(self.cache) < cache_slots: # 꽉 안찼으므로 걍 추가하면 됨
                self.cache.insert(0, page)
            else: #꽉 찼을 때, eviction 하고, 추가하면 됨
                self.cache.pop() #LRU(맨뒤) 제거
                self.cache.insert(0, page) #맨앞에 MRU로 page 추가
        
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)


if __name__ == "__main__":

    data_file = open("./linkbench.trc")
    lines = data_file.readlines() #data_file 의 각 줄을 한개의 요소로 하는 list('\n' 포함)
    for cache_slots in range(100, 1001, 100): #cache slot 100, 200, ... 1000 으로 실험
        cache_sim = CacheSimulator(cache_slots) #지정된 cache slot 으로 CacheSimulator 객체 생성
        for line in lines: # line 하나는 data_file 의 한 줄(공백문자 포함돼 있음)
            page = line.split()[0] #공백문자 벗겨내기; 최종적 str 형
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()

