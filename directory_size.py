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
                return byte_size / 1024
            elif unit == 'MB':
                return byte_size / 1024 ** 2
            elif unit == 'GB':
                return byte_size / 1024 ** 3
            elif unit == 'TB':
                return byte_size / 1024 ** 4
            else:
                return byte_size
        return wrapper

    return inner_func


@convert_unit('MB')
def get_directory_size(path):
    total_size = 0
    for dir_path, sub_dirs, sub_files in os.walk(path):  # Iterating on the directory files & sub-directories.

        for file in sub_files:
            current_path = f"{dir_path}/{file}"
            size = os.path.getsize(current_path)

            logging.debug(f"Path: {current_path}, Size: {size}")
            total_size += size

    return total_size


if __name__ == '__main__':  # Scripting
    path = os.getcwd()  # get Current Working Directory path
    print("Path:", path)
    print("Total size:", get_directory_size(path))
