
class StackArray ():
    def __init__ (self, size):
        self.size = 0
        self.items = [None for i in range(size)]
        self.top = self.items[0]

    def __len__ (self):
        return self.size

    def __str__ (self):
        str_list = "["
        for value in self:
            str_list += f"{value}, "
        str_list += "]"
        str_list = str_list.replace(", ]", "]")

        return str_list

    def __iter__ (self):
        for value in self.items:
            yield value

    def push (self, value):
        if self.size == len(self.items):
            return

        top_index = self.items.index(self.top)

        if self.items[top_index] is not None:
            self.items[top_index + 1] = value
            self.top = self.items[top_index + 1]
        else:
            self.items[top_index] = value
            self.top = self.items[top_index]

        self.size += 1

    def pop (self):
        if self.size < 0:
            return False
        
        top_index = self.items.index(self.top)

        self.items[top_index] = None
        if top_index > 0:
            self.top = self.items[top_index - 1]
        else: 
            self.top = None

        self.size -= 1

    def clear (self):
        while self.top is not None:
            self.pop()

    def find (self, value):
        for arr_value in self:
            if arr_value == value:
                return True

        return False

if __name__ == "__main__":
    stack_arr = StackArray(5)

    for i in range(10):
        stack_arr.push(i)

    print(str(stack_arr))

