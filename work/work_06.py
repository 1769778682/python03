# 使用 for 循环计算字符串 ”H-e--l---l--oP---y--t-hon” 中有多少个字符 ”-”
# 定义一个接收结果的变量
num = 0

for i in 'H-e--l---l--oP---y--t-hon':
    # 计算'-'的数量
    if i == '-':
        num += 1
# 输出‘-’的数量
print(num)
