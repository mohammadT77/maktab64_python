def isprimal(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primals(n):
    # res = []  # !
    for i in range(2, n):
        if isprimal(i):
            yield i
            # res.append(i)
    # return res

def mytest(n):
    prims = primals(n)
    # res = []
    for i in prims:
        yield -i
        # res.append(-i)
    # return res

n = input("Enter a number: ")

prims = mytest(int(n))
for i in prims:
    print(i)