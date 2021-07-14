# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def empty():
    pass


# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# def sum(x):
#     if x>0:
#         pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs(-9))
# print(my_abs('s'))


def pow(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(pow(2, 3))


# 带默认参数的方法
def person(name, age=18):
    print("name: ", name)
    print("age: ", age)


person('wangewi');
person('wangewi', 20)


# 可变参数的方法
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))


def demo(l=[]):
    l.append("END")
    return l


print(demo())
print(demo())
print(demo())


def demo2(l=None):
    if l is None:
        l = []
    l.append("END")
    return l


print(demo2())
print(demo2())
print(demo2())
print(demo(list(range(1, 10))))
print(demo(list(range(1, 10))))
