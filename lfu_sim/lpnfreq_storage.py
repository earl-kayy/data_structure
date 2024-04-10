from lpnFreq import *

# evict 되고 나서도 다시 참조됐을 때, 그 이전까지 있었던 frequency 를 유지해야됨
# cache 에 있는 애들과는 consistency 유지할 필요는 없지만, 나오면서는 마지막 객체 내부 값들의 모습을 기록해야됨
# 다시 힙으로 복귀할 땐 삭제
class Storage:
    def __init__(self):
        self.storage = {}
    
    # 하나의 item 에 대해서 evict 되면 storage 에 넣기
    # 객체를 그대로 유지하기에는 부담이 좀 클수도 있다 생각함
        # 기존 : storage[lpnfreq.getLpn, lpn] ==> 수정 : storage[lpnfreq.getLpn, lpnfreq.getFreq]
    def add(self, lpnfreq):
        self.storage[lpnfreq.getLpn()] = lpnfreq.getFreq()

    # storage 에서 heap 으로 복귀 : lpn 으로 검색해서 옛날에 참조했던 것 있으면 돌려주고, 없으면 None 리턴
    # 힙으로 복귀하는 애는 storage 에서 삭제
    def recover(self, lpn):
        if lpn in self.storage:
            obj = LpnFreq(lpn, self.storage.get(lpn) + 1)
            self.storage.pop(lpn)
            return obj
        else:
            return None
    
    def search(self, lpn):
        if lpn in self.storage:
            return True
        return False

