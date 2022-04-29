from node import Node, SinglyLinkedList
from random import randint

class CircularLinkedList (SinglyLinkedList):
    def append (self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next is not self.head:
                current_node = current_node.next

            current_node.next = new_node

        new_node.next = self.head
        self.size += 1

    def iterator (self):
        current_node = self.head

        for i in range(self.size):
            value = current_node.data
            next_value = current_node.next.data

            current_node = current_node.next

            yield value, next_value

if __name__ == "__main__":
    circular_list = CircularLinkedList()

    for i in range(10):
        circular_list.append(i)

    print(str(circular_list))

    for node, next_node in circular_list.iterator():
        print(f"node: {node}, {next_node}")
