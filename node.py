
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

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

        self.size += 1

    def __len__ (self):
        return self.size

    def iterator (self):
        current_node = self.head

        while current_node is not None:
            value = current_node.data

            current_node = current_node.next

            yield value

    def __str__ (self):
        list_str = "["
        for node_value in self.iterator():
            list_str += f"{node_value}, "
        list_str += "]"
        list_str = list_str.replace(", ]", "]")

        return list_str

    def delete (self, data):
        if self.size <= 0:
            return None

        current_node = self.head
        previous_node = self.head

        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next

                self.size -= 1
                return current_node.data

            previous_node = current_node
            current_node = current_node.next

    def replace (self, value, value_to_replace):
        if self.size <= 0:
            return False

        current_node = self.head
        previous_node = self.head

        replacing_node = Node(value, None)

        while current_node is not None:
            if current_node.data == value_to_replace:
                if current_node == self.head:
                    self.head = replacing_node
                else:
                    previous_node.next = replacing_node

                replacing_node.next = current_node.next

                return current_node.data

            previous_node = current_node
            current_node = current_node.next

    def search (self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                return True

            current_node = current_node.next

        return False

    def append_by_index (self, value, index=0):
        value_index = index

        if self.size == 0:
            value_index = 0
        elif index < 0:
            value_index = (len(self) + 1) - abs(index)

        i = 0

        previous_node = self.head
        current_node = self.head

        new_node = Node(value, None)

        while current_node is not None:
            if i == value_index:
                if current_node == self.head:
                    self.head = new_node
                else:
                    previous_node.next = new_node

                new_node.next = current_node
                self.size += 1
                return

            previous_node = current_node
            current_node = current_node.next
            i += 1

        if value_index > (self.size - 1):
            previous_node.next = new_node
        elif value_index < 0:
            new_node.next = self.head.next
            self.head = new_node

        self.size += 1

    def delete_by_index (self, index):
        if self.size <= 0 or abs(index) > (self.size - 1):
            return False

        index_to_delete = index
        if index < 0:
            index_to_delete = len(self) - abs(index)

        i = 0

        previous_node = self.head
        current_node = self.head

        while current_node is not None:
            if i == index_to_delete:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next

                self.size -= 1
                return current_node

            previous_node = current_node
            current_node = current_node.next
            i += 1

if __name__ == "__main__":
    singly_list = SinglyLinkedList()
    
    for i in range(10):
        singly_list.append(i)

    print(str(singly_list))
