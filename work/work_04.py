# 使用 while 实现一个死循环, 在循环内通过 input() 输入一个数字, 当输入 0 时, 退出循环

# 定义计数器
num = True
# 定义输入变量

while num:
    num_ = int(input('请输入一个数字:'))
    if num_ == 0:
        break
print('循环结束')