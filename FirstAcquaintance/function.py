def printme( str ):
   "打印任何传入的字符串"#函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
   print (str)
   return str
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
print(printme("打印两次吧"))

# -------------参数传递-------------------------

a=[1,2,3]
a="Runoob"

# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
# 而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），
# 可以是 List 类型对象，也可以指向 String 类型对象。

# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
# 而 list,dict 等则是可以修改的对象。
# **********python 传不可变对象实例*********
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b ) # 结果是 2

# **********python 传可变对象实例*********
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist+=[1,2,3,4]
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)


#*************必需参数**************
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str);
   return;
 
#调用printme函数
# printme(); 此处报错



#**********关键字参数*************
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str);
   return;
 
#调用printme函数
printme( str = "菜鸟教程");

# 以下实例中演示了函数参数的使用不需要使用指定顺序：
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;
 
#调用printinfo函数
printinfo( age=50, name="runoob" );

# *********默认参数************

#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;
 
#调用printinfo函数
printinfo( age=50, name="runoob" );
print ("------------------------")
printinfo( name="runoob" );


#************不定长参数*************
# 加了星号（*）的变量名会存放所有未命名的变量参数。
# 如果在函数调用时没有指定参数，它就是一个空元组。
# 我们也可以不向函数传递未命名的变量。如下实例：    

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );



# **********匿名函数************
sum=lambda arg1,arg2:arg1+arg2

print("相加后的值为：",sum(10,20))


# return语句
def sum(arg1,arg2):
    "返回两个参数的和"
    total=arg1+arg2
    print("函数内：",total)
    return total

total=sum(10,20)
print("函数外：",total)


# 变量作用域

x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域


total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total;

#调用sum函数
sum( 10, 20 );
print ("函数外是全局变量 : ", total)


# *********global 和 nonlocal关键字***********
num=1
def func1():
    global num
    print (num)
    num=123
    print(num)
func1()

def outer():
    num=10
    def inner():
        nonlocal num
        num =100
        print(num)
    inner()
    print(num)
outer()