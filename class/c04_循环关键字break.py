# 需求：一共吃5个苹果，胃口较小，吃到第三个吃饱了，提前结束循环。


# 设置计数器
num = 1
# 设置循环条件
while num <= 5:
    # 重复执行代码
    # 判断吃到第三个苹果
    print(f'吃了{num}个苹果')
    if num == 3:
        print('吃饱了，不吃了')
        # 添加break 关键字，结束循环
        break  # 结束循环关键字的添加位置需要格外注意，避免过早结束循环
    # 修改计数器
    num += 1

