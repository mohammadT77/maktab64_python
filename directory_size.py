import logging
import os

logging.basicConfig(level=0)


def convert_unit(unit: str = 'B'):
    unit = unit.upper()

    def inner_func(func):
        def wrapper(*args, **kwargs):
            byte_size = func(*args, **kwargs)

            if unit == 'B':
                return byte_size
            elif unit == 'KB':
                return byte_size // 1024
            elif unit == 'MB':
                return byte_size // 1024 ** 2
            elif unit == 'GB':
                return byte_size // 1024 ** 3
            elif unit == 'TB':
                return byte_size // 1024 ** 4
            else:
                return byte_size
        return wrapper

    return inner_func


# @convert_unit('KB')
def get_directory_size(path):
    total_size = 0
    for i in os.scandir(path):  # Iterating on the directory files & sub-directories.
        i: os.DirEntry  # Typing

        if i.is_file():
            size = os.path.getsize(i.path) # Get file size
        else:
            size = get_directory_size(i.path)  # Recursive directory size

        total_size += size
        # logging.debug(f"Path: {i.path}, size: {size}")

    return total_size


if __name__ == '__main__':  # Scripting
    path = os.getcwd()  # get Current Working Directory path
    print("Path:", path)
    print("Total size:", get_directory_size(path))
