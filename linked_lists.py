class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def deleteWithValue(self, data):
        print('Deleing value :', data)
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


def main():
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(11)
    my_list.append(15)
    my_list.printList()
    my_list.deleteWithValue(11)
    my_list.printList()


if __name__ == '__main__':
    main()
