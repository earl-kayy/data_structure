from minHeap import *
from lpnfreq_storage import *
from lpnFreq import *

def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0
  minheap = MinHeap()
  storage = Storage()
  data_file = open("linkbench.trc")


  for line in data_file.readlines():
    lpn = line.split()[0] #lpn => str 형

    tot_cnt += 1 # 총 참조 횟수 하나 증가
    # lpn_obj = LpnFreq(lpn, 0)
    (lpn_obj, index) = minheap.find(lpn) # lpn 값을 가진 객체가 heap 에 있는지 찾아보기
    # hit 의 경우 (None 이 아니면 힙 안에 존재한다는 뜻)
    # 순서 바뀔수도 있으므로 해당 항 재정렬해야됨(증가한 frequency 위해서)
    if lpn_obj is not None:
      cache_hit += 1
      lpn_obj.addFreq()
      ###다음으로 해볼 것: minHeap 에서 내부적으로 재정렬
      minheap.updateHeap(index)
    # miss 의 경우 -> 다시 가져와야함
    # 꽉 차 있을 경우 -> evict
    # 자리 있을 경우 -> 그냥 삽입
    # storage 에 없고 처음 나오는 애일 경우 -> 새로 객체 생성
    # storage 에 있는 경우 -> storage 에 있는 애로 객체 생성
    else :
      if minheap.size() < cache_slots: # 아직 안 찼을 때 그냥 추가하면 됨
        # storage 에 있으면 그걸로 객체 생성
        if (storage.search(lpn)) : 
          minheap.insert(storage.recover(lpn))
        # storage 에 없으면 새로 객체 생성 (완전 초기)
        else :
          minheap.insert(LpnFreq(lpn, 1))
      else: # 꽉 찼을 때 = eviction(하면서 storage 에 저장)후 삽입해야함
        storage.add(minheap.deleteMin())
        if (storage.search(lpn)) :
          minheap.insert(storage.recover(lpn))
        else:
          minheap.insert(LpnFreq(lpn, 1))
  print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
  for cache_slots in range(100, 1001, 100):
    lfu_sim(cache_slots)
