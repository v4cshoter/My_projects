import os


def find_biggest(path):
    max_size, sec_max_size, file_size = 0, 0, 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
        if file_size > max_size:
            sec_max_size = max_size
            max_size = file_size
        elif file_size > sec_max_size:
            sec_max_size = file_size
    return max_size, sec_max_size


print(find_biggest("./"))
