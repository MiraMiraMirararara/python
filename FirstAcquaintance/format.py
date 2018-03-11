s = 'Hello, Runoob'
print(str(s))
print(repr(s))
 
# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。

for x in range(1, 11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # 注意前一行 'end' 的使用
     print(repr(x*x*x).rjust(4))


for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#  zfill(), 它会在数字的左边填充 0
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))



# ************str.format() 的基本使用如下:************

# 括号及其里面的字符 (称作格式化字段) 
# 将会被 format() 中的参数替换。
print('{}网址:{}'.format('秒回','www.mira.cn'))

# 使用了关键字参数
print('{name}网址: {site}'.format(name='秒回',site='www.mira.cn'))

# 位置及关键字参数可以任意的结合:
print('站点列表 {0},{1},和{other}.'.format('Google','Runoob',other='Taobao'))


# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 
import math 
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名。 
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))


# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。
table={'Google':1,'Runoob':2,'Taobao':3}
for name,number in table.items():
    print('{0:10} ==> {1:10d}'.format(name,number))
# 传入一个字典, 然后使用方括号 '[]' 来访问键值 :
print('Runoob: {0[Runoob]}; Google: {0[Google]}; Taobao: {0[Taobao]}'.format(table))

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 
# 它将左边的参数作为类似 sprintf() 式的格式化字符串,
#  而将右边的代入, 然后返回格式化后的字符串
print('常量 PI 的值近似为：%5.3f。' % math.pi)
print('常量 PI 的值近似为：%6.3f。' % math.pi)