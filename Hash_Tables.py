import random
class Node:
    def __init__(self, name, last_name="" ):
        self.name = name
        self.last_name = last_name
        self.next = None

class HashTable:
    def __init__(self):
        self.keys = {}
        self.list = []

    def add(self, name, last_name):
        person = Node(name, last_name)
        if len(self.list) < 6:
            self.list.append(person)
            person.next = len(self.list) - 1
            self.keys[person.name] = len(self.list) - 1
        else:
            self.keys[name] = random.randint(0, 5)
            self.list[self.keys[name]].next = person
    
    def printList(self):
        for person in self.list:
            print(person.name, person.last_name)

    def getKey(self, name):
        print(self.keys[name])

    def find(self, name):
        key = self.keys[name]
        person = self.list[key]
        while name != person.name:
            if person == None:
                print(name, " not found")
                return False
            person = person.next
        print(person.name, person.last_name)
        return True

def main():   
    my_hash = HashTable()
    my_hash.printList()
    my_hash.add("Fernando", "Alonso")
    my_hash.add("Harry", "Potter")
    my_hash.add("Frodo", "Baggins")
    my_hash.add("Elon", "Musk")
    my_hash.add("Jeff", "Bezos")
    my_hash.add("Red", "Robin")
    my_hash.add("Will", "Smith")
    my_hash.add("Rick", "Riordan")
    print(my_hash.printList())
    my_hash.find("Rick")
    my_hash.find("Fernando")

if __name__ == '__main__':
    main()



