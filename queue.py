class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None or self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.tail
            self.tail.previous = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return None
        out = self.head
        self.head = out.previous
        self.head.next = None

    def printStack(self):
        temp = self.tail
        while temp is not None:
            print(temp.data)
            temp = temp.next


def main():
    my_stack = Stack()
    my_stack.add(10)
    my_stack.add(15)
    my_stack.add(20)
    my_stack.add(25)
    my_stack.printStack()
    print("Pulling")
    my_stack.pop()
    my_stack.printStack()


if __name__ == '__main__':
    main()
