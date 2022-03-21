
from node import Node

class Stack ():
    def __init__ (self):
        self.size = 0
        self.top = None
        self.bottom = None

    def __len__ (self):
        return self.size

    def __str__ (self):
        stack_str = "["
        for node_value in self:
            stack_str += f"{node_value}, "
        stack_str += "]"
        stack_str = stack_str.replace(", ]", "]")

        return stack_str

    def __iter__ (self):
        current_node = self.top

        while current_node is not None:
            value = current_node.data

            current_node = current_node.next

            yield value

    def push (self, value):
        new_node = Node(value)

        if self.top:
            new_node.next = self.top

        self.top = new_node
        self.size += 1

    def pop (self):
        if self.size < 0:
            return False
        
        current_node = self.top

        self.top = current_node.next
        self.size -= 1

        return current_node.data

    def peek (self):
        if self.top:
            return self.top.data
        
        return False

    def clear (self):
        while self.top is not None:
            self.pop()

    def find (self, value):
        current_node = self.top

        while current_node is not None:
            if current_node.data == value:
                return True
            
            current_node = current_node.next

        return False

if __name__ == "__main__":
    stack_list = Stack()

    for i in range(10):
        stack_list.push(i)

    print(str(stack_list))

    print(stack_list.find(2))
