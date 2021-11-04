class ChainOperator(float):
    formula: callable

    @staticmethod
    def __new__(cls, x=...):
        assert hasattr(cls, 'formula'), "An InlineOperator must have a formula"
        return super().__new__(cls, x)

    @classmethod
    def get_operator_class(cls, name: str, formula: callable) -> type:
        t = type(name, (cls,), {})
        t.formula = formula
        return t

    @classmethod
    def make_chain(cls, name=None):
        def inner_func(formula):
            assert callable(formula), "Formula must be callable!"
            return cls.get_operator_class(name or formula.__name__, formula)

        return inner_func

    def __call__(self, x):
        return self.__class__(self.formula(x))


class multi(ChainOperator):
    formula = lambda x, y: x * y


@ChainOperator.make_chain()
def add(x, y):
    return x + y
print(type(add(10)))

t = ChainOperator.get_operator_class('test', lambda x, y: x ** y)

print(t(2)(3)(2))
