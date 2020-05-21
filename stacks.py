class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        out = self.head
        self.head = out.next

    def printStack(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


def main():
    my_stack = Stack()
    my_stack.add(10)
    my_stack.add(15)
    my_stack.add(20)
    my_stack.printStack()
    print("Pulling")
    my_stack.pop()
    my_stack.printStack()


if __name__ == '__main__':
    main()
