class MyLover(object):
    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            MyLover._instance = super(MyLover, cls).__new__(cls)
        return cls._instance


lover1 = MyLover()
lover2 = MyLover()
print lover1 is lover2


def singleton(cls, *args, **kwargs):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner


@singleton
class MyLove(object):
    def __init__(self):
        pass


love1 = MyLove()
love2 = MyLove()
print love1 is love2
