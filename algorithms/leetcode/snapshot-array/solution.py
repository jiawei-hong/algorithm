class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snapshot = [[(0,0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshot = self.snapshot[index]

        l, r = 0, len(snapshot) - 1

        while l <= r:
            m = (l + r) // 2

            if snapshot[m][0] <= snap_id:
                l = m + 1
            else:
                r = m - 1
        return snapshot[r][1]