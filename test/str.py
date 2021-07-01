print('包含中文的str')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('a'))
print(chr(97))
print(ord('中'))

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
print(b'abc')

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
#
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print('ABC'.encode('ascii'))
print('王伟'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe7\x8e\x8b\xe4\xbc\x9f'.decode('utf-8'))
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe7\x8e\x8b\xe4\xbc\x9f'.decode('utf8', errors='ignore'))

print(len('ABC'))
print(len('王伟'))
print(len(b'ABC'))
print(len('王伟'.encode('utf-8')))
print("hello %s" % 'wangwei')