class MyIterClass:  # Iterable!

    def __iter__(self):
        return 123

    # def __next__(self):
    #     self.n += 1
    #     if self.n > 10:
    #         raise StopIteration()
    #     return self.n


# m_iter = iter(MyIterClass())
# print(m_iter)
# print(next(m_iter)) # a
# print(next(m_iter)) # s
# print(next(m_iter))

def avg(*args):
    return sum(args) / len(args)

def register_user(*args, **kwargs):
    print(kwargs)

register_user(1,2,3,4,5,5,6,7,7, name='sdsadsa', email='asdsada', age=123)
