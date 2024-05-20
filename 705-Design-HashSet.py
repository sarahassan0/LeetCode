class MyHashSet:
    def __init__(self):
        self.Set = defaultdict(int)

    def add(self, key: int) -> None:
        self.Set[key]  = True


    def remove(self, key: int) -> None:
        if key in self.Set:        
            self.Set[key] = False


    def contains(self, key: int) -> bool:
        if self.Set[key]:
            return self.Set[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)