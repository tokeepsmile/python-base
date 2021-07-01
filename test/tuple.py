
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmates = ('Michael', 'Bob', 'Tracy')
print(len(classmates))
print(classmates[0])
t = (1)
print(type(t))
t = (1,)
print(type(t))

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
