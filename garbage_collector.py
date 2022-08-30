"""
当程序不再需要一个 Python 对象时，系统必须把该对象所占用的内存空间释放出来，这个过程被称为垃圾回收（GC，Garbage Collector），
Python 会自动回收所有对象所占用的内存空间.
当一个对象被垃圾回收时，Python 就会自动调用该对象的 __del__ 方法。需要说明的是，不要以为对一个变量执行 del 操作，
该变量所引用的对象就会被回收，只有当对象的引用计数变成 0 时，该对象才会被回收。
因此，如果一个对象有多个变量引用它，那么 del 其中一个变量是不会回收该对象的。
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __del__(self):
        print('del删除对象')


im = Item("test", 19.98)
x = im
m = im

print("++++++++++++++++")
del x
print("----------------")
print(im.price)