from Utils import hash1, hash2

class bloomFilter:
    
    def __init__(self, filter_size: int):
        self.bloom_filter = filter_size * [0]
        self.filter_size = filter_size
    
    def insert_flow(self, flow: tuple[str, str, int, int , str]):
        idx1: int = hash1(flow=flow, filter_size=self.filter_size)
        idx2: int = hash2(flow=flow, filter_size=self.filter_size)
        self.bloom_filter[idx1] = 1
        self.bloom_filter[idx2] = 1

    def check_flow_exist(self, flow: tuple[str, str, int, int , str]):
        idx1: int = hash1(flow=flow, filter_size=self.filter_size)
        idx2: int = hash2(flow=flow, filter_size=self.filter_size)
        if self.bloom_filter[idx1] and self.bloom_filter[idx2]:
            return True
        else:
            return False
    
    
            