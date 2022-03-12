
from random import randint
from arr_in_python import Array

class Array_2D (Array):
    def __init__ (self, width=1, height=1, fill_value=None):
        self.size = width * height
        self.items = [[] for i in range(height)]
        
        for row_index in range(height):
            self.items[row_index] = [fill_value for i in range(width)]

    def __get_height__ (self):
        return len(self.items)

    def __get_width__ (self):
        return len(self.items[0])

    def __get_size__ (self):
        return self.size

    def __get_row__ (self, index):
        return self.items[index]

    def __get_value__ (self, index_row, index_value):
        return self.items[index_row][index_value]

    def __str__ (self):
        string = ""

        for row in self.items:
            for value in row:
                string += f"{value} "

            string += "\n"

        return string

    def __change_values__ (self, value=0):
        for i in range(len(self.items)):
            for j in range(len(self.items[i])):
                self.items[i][j] = value

if __name__ == "__main__":
    matrix = Array_2D(5, 5)

    matrix.__change_values__(10)
    print(matrix.__str__())
