import re

line = "aegoog8897"
# ^代表一什么开头  .表示匹配任何内容  * 表示重复任意内容  ?表示一什么结尾  ()表示提取子串  ？表示非贪懒模式匹配  Python默认是贪懒匹配从右边匹配
# + 表示某个字符至少出现一次  {} 表示某个字符出现的次数 列入：{2,5}表示至少出现2次最多出现5次   {2,}表示至少2次及2次以上
# | 代表或的关系满足一个条件就行  [] 代表任何包含在[]内的都可以匹配
# \s 代表匹配空格   \S 匹配非空格  \w 匹配任意字符 \W 匹配非满足任意字符 \d表示匹配数字
reg = "^a.*7$"

if re.match(reg, line):
    print("yes")

# str = "boooooooobjbsl3699"
# str = "booby123"
# str = "hi hello"
# str = "study in 中国清华大学"
str = "xx出生于2018年"
# str = "18790608789"
# mathReg = ".*?(b.*?b).*"
# mathReg = ".*(b.+b).*"
# mathReg = ".*(b.{5,}b).*"
# mathReg = "((boo|booby)123)"
# mathReg = "(1[6943587][0-9]{9})"
# mathReg = "(1[6943587][^1]{9})"
# mathReg = "(hi[A-za-z0-9_]hello)"
# mathReg = "(hi\Whello)"
# mathReg = ".*?([\u4e00-\u9fa5]+大学)"
mathReg = ".*?(\d+)年"
math_obj = re.match(mathReg, str)
if math_obj:
    print(math_obj.group(1))