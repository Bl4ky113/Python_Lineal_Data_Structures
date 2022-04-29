
from random import randint

class Array ():
    def __init__ (self, size=0, fill_value=None):
        self.size = size
        self.items = [fill_value for i in range(size)]

    def random_values (self, min_val, max_val):
        self.items = [randint(min_val, max_val) for i in range(self.size)]

    def sum_values (self):
        return sum(self.items)

def main ():
    obj_arr = Array(5, 0)
    print(obj_arr.items)
    obj_arr.random_values(0, 10)
    print(obj_arr.items)
    print(obj_arr.sum_values())

if __name__ == "__main__":
    main()
