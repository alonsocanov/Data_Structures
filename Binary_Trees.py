class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.value)
        if self.right is not None:
            self.right.printInOrder()


def main():
    my_tree = Node(10)
    my_tree.insert(5)
    my_tree.insert(15)
    my_tree.insert(8)
    my_tree.printInOrder()
    print(my_tree.contains(5))
    print(my_tree.contains(6))


if __name__ == '__main__':
    main()
