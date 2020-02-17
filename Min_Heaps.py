class MinIntHeap:
    def __init__(self):
        self.items = []
        self.size = 0 

    def getLeftChildIndex(self, parent_index):
        return 2 * parent_index + 1
    def getRightChildIndex(self, parent_index):
        return 2 * parent_index + 2
    def getParentIndex(self, child_index):
        return int((child_index - 1) / 2)
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]
    def leftRight(self, index):
        return self.items[self.getRightChildIndex(index)]
    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, index_1, index_2):
        temp = self.items[index_1]
        self.items[index_1] = self.items[index_2]
        self.items[index_2] = temp

    def peek(self):
        if self.size == 0:
            return "Not possible"
        return items[0]

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and (self.parent(index) > self.items[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smaller_child_index = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.RightChild(index) < self.leftChild(index):
                smaller_child_index = self.getRightChildIndex(index)
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

    def poll(self):
        if self.size == 0:
            return "Not possible"
        item = self.items[0]
        items[0] = items[size - 1]
        self.size -= 1
        heapifyDown()
        return item

    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapifyUp()

def main():
    my_heaps = MinIntHeap()
    my_heaps.add(10)
    my_heaps.add(15)
    my_heaps.add(20)
    my_heaps.add(17)
    my_heaps.add(8)
    my_heaps.add(25)
    print(my_heaps.items)

if __name__ == '__main__':
    main()