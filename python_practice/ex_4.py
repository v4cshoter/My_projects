class MyIterator:
    def __init__(self, values):
        if isinstance(values, (list, tuple, str)):
            self.max_values = values
        elif isinstance(values, dict):
            self.max_values = values.values()
        else:
            raise ValueError("Invalid input type")

        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < len(self.max_values):
            self.current_value += 1
            return self.max_values[self.current_value - 1]
        else:
            raise StopIteration


my_iter = MyIterator("wis")
for i in my_iter:
    print(i)
# print(my_iter.__next__())
