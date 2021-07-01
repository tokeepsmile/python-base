# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[0])
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
classmates.append('Adam')
print(len(classmates))
classmates.insert(1, 'Jack')
print(classmates)
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][0])