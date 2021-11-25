import logging
import os


# logging.basicConfig(level=0)

def convert_unit(unit, byte_size):
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


def convert_unit_dec(unit: str = 'B'):
    unit = unit.upper()

    def inner_func(func):
        def wrapper(*args, **kwargs):
            byte_size = func(*args, **kwargs)
            return convert_unit(unit, byte_size)

        return wrapper

    return inner_func


# @convert_unit_dec('MB')
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
    import argparse

    parser = argparse.ArgumentParser(description="Directory size calculator utility.")

    # dir_path:
    parser.add_argument(dest='path', type=str, default=os.getcwd(), nargs='?',
                        help='Directory path')
    # unit:
    parser.add_argument('-u', '--unit', type=lambda s: s.upper(), default='B',
                        choices=('B', 'KB', 'MB', 'GB', 'TB'),
                        help="Size unit")

    args = parser.parse_args()

    size = get_directory_size(args.path)

    print("Path:", args.path)
    print("Total size:", convert_unit(args.unit, size), args.unit)
