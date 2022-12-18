def f(x):
    def f1(*args, **kwargs):
        print("*" * 5)
        x(*args, **kwargs)
        print("*" * 5)
    return f1
def a(x):
    def f1(*args, **kwargs):
        print("%" * 5)
        x(*args, **kwargs)
        print("%" * 5)
    return f1

@f
@a
def p(m):
    print(m)

p("hello")