import pyscreenshot
import argparse


def save_screenshot(dirpath="my_sc/", name='my_sc', ext='.png'):
    my_sc = pyscreenshot.grab()
    save_path = dirpath + name + ext
    with open(save_path, 'wb') as f:
        my_sc.save(f)
    return save_path


if __name__ == '__main__':  # Script!!!!!
    parser = argparse.ArgumentParser()  # parser instance

    parser.add_argument('-d', '--dir', type=str, help="Directory path", default='')
    parser.add_argument('-n', '--name', type=str, help="File name", default='my_sc')
    parser.add_argument('-e', '--ext', type=str, help="File extension", default='.png')

    args = parser.parse_args()  # dir, name, ext

    save_path = save_screenshot(args.dir, args.name, args.ext)
    print("Saved at:", save_path)
