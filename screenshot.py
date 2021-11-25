import pyscreenshot


def save_screenshot(path="my_sc.png"):
    my_sc = pyscreenshot.grab()
    with open(path, 'wb') as f:
        my_sc.save(f)
    return True


if __name__ == '__main__':  # Script!!!!!
    print('Akbar')
    print('Asqar')
    save_screenshot()
