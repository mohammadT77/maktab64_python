def make_upper(func):  # func = hello_word
    def inner_function():  # wrapper function
        res = func()  # hello_world() -> "Hello World!"
        return res.upper()  # "HELLO WORLD"

    return inner_function

@make_upper
def hello_world():
    return "Hello World!"

@make_upper  # make_upper(test)
def test():
    return "dsdsadasda adassdsada"


print(hello_world())

# old_function = hello_world
# new_function = make_upper(hello_world) # func (callable)

# print('old:', old_function())
# print('new:', new_function())  # HELLO WORLD