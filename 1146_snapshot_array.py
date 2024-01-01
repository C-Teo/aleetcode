# https://leetcode.com/problems/snapshot-array/

# WIP

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0]*length
        self.snaps = {}
        self.num_snaps = -1

    def set(self, index: int, val: int) -> None:
        if index > -1 and index < len(self.arr):
            self.arr[index] = val

    def snap(self) -> int:
        self.num_snaps += 1
        for index,val in enumerate(self.arr):
            if val != 0:
                self.snaps[str(self.num_snaps)+str(index)] = val
        return self.num_snaps

    def get(self, index: int, snap_id: int) -> int:
        key = str(self.num_snaps)+str(index)
        if key in self.snaps:
            return self.snaps[key]
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)