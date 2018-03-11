f = open("/tmp/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()


# 打开一个文件
f = open("/tmp/foo.txt", "r")
# 调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
str1 = f.read()
print(str1)

# 关闭打开的文件
f.close()


# f.readline()从文件中读取单独的一行。换行符为 '\n'。f.readline() 
# 如果返回一个空字符串, 说明已经已经读取到最后一行。
f=open("/tmp/foo.txt","r")
str1=f.readline()
print(str1)
f.close()

# f.readlines()返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。

f = open("/tmp/foo.txt", "r")

str1 = f.readlines()
print(str1)

# 关闭打开的文件
f.close()


# 另一种方式是迭代一个文件对象然后读取每行:
f=open("/tmp/foo.txt","r")
for line in f :
    print(line,end=' ')
f.close()

# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
f=open("/tmp/foo.txt","w")
num=f.write("Python 是一个非常好的语言. \n是的,的确非常好!!\n")
print(num)
f.close()

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
f=open("/tmp/foo1.txt","w")
value =('www.runoob.com',14)
s=str(value)
f.write(s)
f.close()


f=open('/tmp/foo.txt','rb+')
print(f.write(b'0123455789abcdef'))
print(f.seek(5))
f.seek(-3, 2)
print(f.read(1))


import pickle,pprint

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()