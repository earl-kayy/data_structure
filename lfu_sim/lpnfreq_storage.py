from lpnFreq import *

# program 이 진행되는 동안, 객체의 frequency 를 기록하기 위한 클래스 (evict 이후, cache로 다시 들어갈 경우 필요)
# cache 에 현재 있는 애들과 consistency 유지할 필요는 없지만, 캐시에서 나오면서는 마지막 객체 내부 값들의 모습을 여기에 기록해야됨
# 다시 힙으로 복귀할 땐 삭제
class Storage:
    def __init__(self):
        # 객체 자체를 보관하기엔 프로그램이 모든 lpn 에 대한 객체를 진행 동안 가지고 있어야하므로 값만 딕셔너리 형태로 보관
        self.storage = {}
    
    # 하나의 item 에 대해서 evict 되면 storage 에 넣기
    def add(self, lpnfreq):
        self.storage[lpnfreq.getLpn()] = lpnfreq.getFreq()

    # storage 에서 heap 으로 복귀 : lpn 으로 검색해서 옛날에 참조했던 것 있으면 객체로 새로 만들어서 돌려주고, 없으면 None 리턴
    # 힙으로 복귀하는 애는 storage 에서 삭제
    def recover(self, lpn):
        if lpn in self.storage:
            # storage 에서 heap 으로 복귀하면서 freq 하나 증가함 : 다시 참조된 것이므로
            obj = LpnFreq(lpn, self.storage.get(lpn) + 1)
            self.storage.pop(lpn)
            return obj
        else:
            return None
    # lpn 이 cache 에 없을 때, 참조된 적이 한번이라도 있는지 확인위한 함수
    def search(self, lpn):
        if lpn in self.storage:
            return True
        return False

