class CountingTableEntry:
    def __init__(self, FlowXor, FlowCount, PacketCount):
        self.FlowXOR = FlowXor
        self.FlowCount = FlowCount
        self.PacketCount = PacketCount

class CountingTable:
    
    