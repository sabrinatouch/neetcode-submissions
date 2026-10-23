class MyHashMap:

    def __init__(self):
        """
        """
        self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        """
            If the key already exists in the map,
            update the corresponding value

            If the key doesn't already exist in the map,
            add the corresponding value into map
        """
        self.map[key] = value

    def get(self, key: int) -> int:
        """
            if the map does not contain the key,
                return -1
            return int, corresponding value of the key that's passed in
        """
        if self.map[key] is None:
            return -1
        else:
            return self.map[key]

    def remove(self, key: int) -> None:
        """
            if the map contains the key
            remove key and corresponding value 
        """
        self.map[key] = None
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)