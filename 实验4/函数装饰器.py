def debug(func):
    def wrapper():
        # 定义一个内部函数wrapper，它将打印调试信息并返回func的执行结果
        print("[DEBUG]: enter {}()".format(func.__name__))
        # 打印进入函数的调试信息，包括函数的名称
        return func()

    return wrapper()  # 返回wrapper函数的执行结果，而不是wrapper函数本身


@debug
def say_hello():
    # 使用debug装饰器，它会在say_hello函数执行前打印调试信息
    print("hello")


say_hello()  # 调用say_hello函数，由于装饰器的作用，会先打印调试信息


@debug
def say_goodbye():
    # 使用debug装饰器，它会在say_goodbye函数执行前打印调试信息
    print("goodbye")


say_goodbye()  # 调用say_goodbye函数，由于装饰器的作用，会先打印调试信息
