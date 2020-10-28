# for循环遍历'Python'
# for + else搭配使用
for i in 'Python':
    print(i)
else:
    print('循环结束后会执行的代码')
print('xxx')
# for + break + else
for i in 'Python':
    if i == 'h':
        break
    print(i)
else:
    print('循环结束后会执行的代码')
print('xxx')
# for + continue + else
for i in 'Python':
    if i == 'h':
        continue
    print(i)
else:
    print('循环结束后会执行的代码')
print('xxx')
# while 循环也可以和else搭配使用，使用效果基本和for和else使用效果一样
