# 1.A
s = input("Enter the problem: ")
print("Result:", eval(s))


# 1.B
def shift(l: list, i: int) -> list:
    i %= len(l)
    return l[i:] + l[:i]


# 1.C
l1, l2 = [1, 2, 3, 4], [2, 6, 3, 2]
# res1 = [x*y for x,y in zip(l1, l2)]  # Solution 1
res2 = list(map(lambda x: x[0] * x[1], zip(l1, l2)))  # Solution 2
print(res2)
