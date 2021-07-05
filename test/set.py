# set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key。
# 要创建一个 set，需要提供一个 list 作为输入集合：
s = set(range(1, 11))
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

# set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 上面我们讲了，str 是不变对象，而 list 是可变对象。
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)

a = 'abc'
a.replace('a', 'A')
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)