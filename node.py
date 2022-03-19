
from random import randint

class Node ():
    def __init__ (self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList ():
    def __init__ (self):
        self.head = None
        self.size = 0

    def append (self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node

        self.size += 1

    def len (self):
        return self.size

    def iterator (self):
        current_node = self.head

        while current_node:
            value = current_node.data

            current_node = current_node.next

            yield value

    def delete (self, data):
        if self.size <= 0:
            return None

        current_node = self.head
        previous_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                elif current_node == None:
                    return None
                else:
                    previous_node.next = current_node.next
                    self.size -= 1

                    return current_node.data

            previous_node = current_node
            current_node = current_node.next

def ez_print():
    print("---")
    print_output = ""
    for value in singly_list.iterator():
        print_output += f"{value}, "
    print(print_output)

if __name__ == "__main__":
    singly_list = SinglyLinkedList()
    
    for i in range(3):
        singly_list.append(i ** 2)
   
    ez_print()

    print("---")
    print(singly_list.len())

    singly_list.delete(9)
    singly_list.delete(121)
    singly_list.delete(144)

