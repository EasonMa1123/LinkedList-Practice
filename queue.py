class queue:
    def __init__(self, size):
        self.__arr = [None] * size
        self.__size = size
        self.__head = 0
        self.__tail = 0
        self.__count = 0

    def append(self, value):
        if self.__count == self.__size:
            return -1  # overflow
        
        self.__arr[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__size
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            return -1  # underflow
        
        item = self.__arr[self.__head]
        self.__arr[self.__head] = None
        self.__head = (self.__head + 1) % self.__size
        self.__count -= 1
        return item

    def isEmpty(self):
        return self.__count == 0

    def printQueue(self):
        return self.__arr

    def getHead(self):
        if self.__count == 0:
            return None
        return self.__arr[self.__head]

    def getTail(self):
        if self.__count == 0:
            return None
        return self.__arr[(self.__tail - 1) % self.__size]
