class MyIterClass:  # Iterable!

    def __iter__(self):
        return 123

    # def __next__(self):
    #     self.n += 1
    #     if self.n > 10:
    #         raise StopIteration()
    #     return self.n


m_iter = iter(MyIterClass())
print(m_iter)
print(next(m_iter)) # a
print(next(m_iter)) # s
print(next(m_iter))

