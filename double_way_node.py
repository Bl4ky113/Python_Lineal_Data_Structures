from node import Node

class DoubleWayNode (Node):
    def __init__ (self, data, prev_node=None, next_node=None):
        super().__init__(data, next_node)
        self.prev = prev_node

class DoubleLinkedList ():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def append (self, data, reverse=True):
        new_node = DoubleWayNode(data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else: 
            current_node = self.head

            while current_node.next is not self.head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node


        self.tail.next = self.head
        self.head.prev = self.tail
        self.size += 1

    def __len__ (self):
        return self.size

    def iterator (self, reverse=False):
        list_init = "head"
        list_next = "next"

        if reverse:
            list_init = "tail"
            list_next = "prev"

        current_node = getattr(self, list_init)

        for i in range(self.size):
            value = current_node.data

            current_node = getattr(current_node, list_next)

            yield value

    def __str__ (self, reverse=False):
        list_str = "["
        for node_value in self.iterator(reverse):
            list_str += f"{node_value}, "
        list_str += "]"
        list_str = list_str.replace(", ]", "]")

        return list_str

    def delete (self, value):
        if self.size == 0:
            return False

        current_node = self.head

        for i in range(self.size):
            if current_node.data == value:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

                self.size -= 1
                return current_node.data

            current_node = current_node.next

        return False

    def find (self, value):
        if self.size == 0:
            return False

        for node_value in self.iterator():
            if node_value == value:
                return True

        return False

    def replace (self, value, value_to_replace):
        if self.size == 0:
            return False

        current_node = self.head

        replacing_node = DoubleWayNode(value, None, None)

        for i in range(self.size):
            if current_node.data == value_to_replace:
                if current_node == self.head:
                    self.head = replacing_node

                if current_node == self.tail:
                    self.tail = replacing_node

                replacing_node.next = current_node.next
                replacing_node.prev = current_node.prev
                
                current_node.next.prev = replacing_node
                current_node.prev.next = replacing_node

                return current_node.data

            current_node = current_node.next


if __name__ == "__main__":
    double_list = DoubleLinkedList()

    for i in range(10):
        double_list.append(i)

    print(str(double_list))

    double_list.replace(555, 0)

    print(str(double_list))


