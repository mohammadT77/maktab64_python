class range:

    def __init__(self, start, end: int = None, step = 1) -> None:
        if end is None:
            start, end = 0, start

        assert step != 0, "Step cannot be 0 (inf loop)"

        self.__start = start
        self.__end = end
        self.__step = step

    def __iter__(self):
        self.__i = self.__start
        return self

    def __next__(self):
        res = self.__i
        if res < self.__end:
            self.__i += self.__step
            return res
        else:
            raise StopIteration()

