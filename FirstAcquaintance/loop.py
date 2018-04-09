count = 0
while (count < 9):
   print ('The count is:', count)
   count += 1
 
print ("Good bye!")


i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print (i)         # 输出双数2、4、6、8、10
 
i = 1
while 1:            # 循环条件为1必定成立
    print (i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break


#-------无限循环--------
var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = input("Enter a number  :")
   print ("You entered: ", num)
   if int(num) == 0: break
print ("Good bye!")


#----------------循环使用 else 语句------------
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
#------------简单语句组--------------

# flag = 1
 
# while (flag): print ('Given flag is really true!')
 
# print ("Good bye!")


#-----------------for 遍历-------
for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果 :', fruit)
 
print ("Good bye!")

#-----------通过序列索引迭代------------
fruits=['banana','apple','mango']
for index in range(len(fruits)):
    print('当前水果：',fruits[index])
print('Good bye!')

#------------循环使用 else 语句------------
for num in range(10,20):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print('%d 等于 %d * %d'%(num,i,j))
            break
    else:print(num,'是一个质数')


#-------------- 循环嵌套------------------
 
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break #  相当于 i%j==0
      j = j + 1
   if (j > i/j) : print (i, " 是素数")
   i = i + 1
 
print ("Good bye!")

#---------------pass 语句----------------!!!!这个是好东西呐，相当于continue，但可以有自定义的代码块
for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   print ('当前字母 :', letter)

print ("Good bye!")

res=0
for i in range(1,2,10):
    res+=i
print(res)


source =['aaaaaa','bbbbbb','cccccc','ddddd','cccccc']
print('有趣的推导式1')
print([i for i in source])#列表推导式
print((i for i in source))#生成器推导式 可以少一组括号 没区别
print({i for i in source})#集合推导式
print({i:i for i in source})#字典推导式

#没有tuple推导式 但你可以通过下面的方式
print(tuple(i for i in source))#利用生成器推导式 转换成元组 


print('没什么特别的纯粹做试验')
print([(i for i in source)])
print({(i for i in source)})
print([[i for i in source]])
# print({[i for i in source]})  TypeError: unhashable type: 'list'


# print(i) for i in source 外面不加[] 语法错误 SyntaxError: invalid syntax
print('在最外面加[]')
[print(i) for i in source] #这个很有趣 在另一篇文章里面使用了这个
#这里的print 可以是任何的函数 效果是类似的

print('试试最外面 用（）或者{}')
(print(i) for i in source)#输出空 
{print(i) for i in source}#这个和中括号效果一样！！


print('那如果i周围没有括号呢？？')
#没有括号之后 print里面就是一个迭代器 外面加括号 没什么作用 大概相当于数学里面（1+2）=[1+2]={1+2} =1+2 
[print(i for i in source)]
(print(i for i in source))
{print(i for i in source)}
