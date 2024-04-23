def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func

    return wrapper()


@debug
def say_hello():
    print("hello")


say_hello()


@debug
def say_goodbye():
    print("goodbye")


say_goodbye()
