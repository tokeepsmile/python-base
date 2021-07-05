d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Adam'] = 67
print(d['Adam'])
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# 要避免 key 不存在的错误，有两种办法，一是通过in判断 key 是否存在：
if 'Jack' in d:
    print(d.get('Jack'))