class Site:
    def __init__(self, name, url):
        self.name = name
        self._url = url

    def who(self):
        print('name:', self.name)
        print('url:', self._url)

    def __foo(self):
        print("这是私有方法")

    def foo(self):
        print("这是公共方法")
        self.__foo()


x = Site("python教程", "http://www.baidu.com")
x.who()
x.foo()
x.__foo()

