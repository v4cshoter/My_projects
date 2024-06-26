def range_number(arr):
    for s in arr[::-1]:
        yield len(s)


my_list = ["one", "two", "three", "long number"]
for i in range_number(my_list):
    print(i, end=" ")
