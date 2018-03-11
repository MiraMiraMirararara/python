class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5


# 类的方法与普通的函数只有一个特别的区别——
# 它们必须有一个额外的第一个参数名称,
# 按照惯例它的名称是 self,self 代表的是类的实例。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t=Test()
t.prt()

class people :
    #定义基本属性
    name=''
    age=0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight =0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w        
    def speak(self):
        print("%s 说：我%d 岁。"%(self.name,self.age))
        print(self.__weight)
        print(self._people__weight)
# 实例化类
p=people('runoob',10,30)
p.speak()

class student (people):
    grade=''
    def __init__(self,n,s,w,g):
        #调用父类的构造函数
        people.__init__(self,n,s,w)
        self.grade=g
    #覆写父类的方法
    def speak(self):
        print("%s 说：我%d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
s = student('ken',10,60,3)
s.speak()

class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫 %s ，我是一个演说家，我演讲的主题是%s "%(self.name,self.topic))


#多重继承
class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test=sample('Tim',25,80,4,"Python")
test.speak()#方法名相同，默认调用的是在括号中排前的父类的方法
# print(test.__weight)
print(test._people__weight)#私有变量可以用这种方式访问

class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private
 
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
 
    def __foo(self):          # 私有方法
        print('这是私有方法')
 
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
# x.__foo()      # 报错

#运算符重载
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):#！！！！！！很有用啊啊啊啊啊
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)