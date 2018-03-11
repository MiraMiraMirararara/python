
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print (counter)
print (miles)
print (name)
a = b = c = 1
b=2
e, f, g = 1, 2, "john"
print(a)
print(b)
print(c)
print(e)
print(f)
print(g)

intA =1
# longA=51924361L    python3中只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
compA=1+3j
floatA=0.789
print('intA',intA)
# print('longA',longA)
print('compA',compA)
print('floatA',floatA)

#-----------------Sting
str = 'Hello World!'
 
print (str)           # 输出完整字符串
print (str[0])        # 输出字符串中的第一个字符
print (str[2:7] )     # 输出字符串中第三个至第五个之间的字符串
print (str[2:])      # 输出从第三个字符开始的字符串
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串

#-----------------List
list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list1)               # 输出完整列表
print (list1[0])            # 输出列表的第一个元素
print (list1[1:3])          # 输出第二个至第三个元素 
print (list1[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print (list1 + tinylist)    # 打印组合的列表

#---------------------Tuple 元组
 
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第三个的元素 
print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)       # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组

#--------------------Tuple & List
 
tuple1 = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list2 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple1[2] = 1000    # 元组中是非法应用
list2[2] = 1000     # 列表中是合法应用

 
#--------------dictionary字典 
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print (dict['one'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值
#------------- 集合（set）是一个无序不重复元素的序列。---------------
'''
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
 
print(a - b)     # a和b的差集
 
print(a | b)     # a和b的并集
 
print(a & b)     # a和b的交集
 
print(a ^ b)     # a和b中不同时存在的元素

a='123'
b=int(a)
print(b)  
print(isinstance(b, int))

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A)) # returns True
print(type(A()) == A)     # returns True
print(isinstance(B(), A))   # returns True
print(type(B()) == A)        # returns False


number = 0xA0F#十六进制
print(number)
number=0o37 # 八进制
print(number)
print('askdfjklasasdf\tegerg\naskdfjklasasdf\tegerg')
print (r'\n')
#------------字符串格式化------------
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

str='happy  birthday!'
print(str.capitalize())

a=1000000.0
print("%g"%(a))
print("%f"%(a))
print("%e"%(a))

a=list(range(5))
print(a)