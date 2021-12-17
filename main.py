def is_primal(x):
    for i in range(2, x):
        if x % i == 2:
            return False

    return True

print(int('111'))