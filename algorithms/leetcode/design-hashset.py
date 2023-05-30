class MyHashSet:

    def __init__(self):
        self.stack = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.stack[key] = True

    def remove(self, key: int) -> None:
        self.stack[key] = False

    def contains(self, key: int) -> bool:
        return self.stack[key]