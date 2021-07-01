import re


str = "XXX出生于2018年6月1日"
# str = "XXX出生于2018/6/1"
# str = "XXX出生于2018-6-1"
# str = "XXX出生于2018-06-01"
# str = "XXX出生于2018-06"

mathReg = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|$)).*"
math_obj = re.match(mathReg, str)
if math_obj:
    print(math_obj.group(1))