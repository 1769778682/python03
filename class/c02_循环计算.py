# 计算0-100所有整数累加和结果
# 定义存储结果值的变量
result = 0
# 定义计数器
num = 0
# 设置循环条件
while num <= 5:
    # 进行运算
    # result = result + num
    result += num
    # 处理计数器
    # num = num + 1
    num += 1
print(f'0-100累加和为：{result}')
# 注意：
# 1.累加结果的变量名位置不可互换
# 2.result = result + num 等价于result += num