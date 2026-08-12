class MyHashSet:

    def __init__(self):
        self.set = {}
        print(self.set)
    
    def add(self, key: int) -> None:
        if self.set.get(key):
            return
        self.set[key] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.pop(key)


    def contains(self, key: int) -> bool:
        if key in self.set:
            return True
        return False
        
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)