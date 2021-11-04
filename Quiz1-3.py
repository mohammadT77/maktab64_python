from functools import reduce


def primal_divisors(n: int):
    res = []  # Append primal divisors!
    while n > 1: # 16 -> 8 -> 4 -> 2
        for i in range(2, n):
            if n % i == 0:  # Is divisible!!!
                res.append(i)
                n //= i  # n = n // i
                break
    return res


def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# # is_prime TESTs -> GOOD
# print(is_prime(10))
# print(is_prime(20))
# print(is_prime(4))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(7))
# print(is_prime(11))
#
# Primal divs Tests -> GOOD!
for n in range(2, 100):
    divs = primal_divisors(n)
    res = reduce(lambda x, y: x * y, divs)  # Zarbe DIVS
    if res!=n or not all(map(is_prime, divs)):
        print("INVALID!!!!!!!!")
        break
    divs_set = set(divs)
    print(n, '*'.join([(f"{d}^{divs.count(d)}" if divs.count(d) > 1 else f"{d}") for d in divs_set]))  # 2^3 * 3
else:
    print("Function works correctly!")



