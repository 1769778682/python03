# 使用 while 循环实现一个范围在 0-10 之间的猜数游戏
# 说明:
# 1. 通过随机方法生成一个 0-10 之间的数字
# 2. 通过 input() 函数输入一个数字
# 3. 比较两个数字, 输入数字 > 随机数字, 提示猜大了; 输入数字 < 随机数字, 提示猜小了.
# 4. 直到输入数字等于随机数字, 提示猜数次数, 结束循环

# 导包
import random


# 定义计数器
num = 0
while True:
    user = int(input('请输入您的数字:'))
    computer = random.randint(0, 10)
    if user > computer:
        print(f'您猜大了哟，随机数是{computer}')
        num += 1
    elif user < computer:
        print(f'您猜小了呦，随机数是{computer}')
        num += 1
    else:
        print('恭喜您，猜对了！')
        num += 1
        break
print(f'您总共对局{num}局')

