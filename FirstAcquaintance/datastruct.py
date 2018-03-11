from collections import deque
# 列表

list1=[1,2,3]
list2=[2,4,5,6]
list1.extend(list2)
print(list1)
print(list1.count(2))
list1.append(7)
print(list1)
list1.insert(2,666)
print(list1)
list1.remove(666)
print(list1)
list1.pop()
print(list1)
list1.sort()
print(list1)
list1.clear()  #del list1[:]
print(list1)


# 将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)
#*************************队列**********************************
# 列表方法使得列表可以很方便的作为一个堆栈来使用，
# 堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。
# 用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to ar   rive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                         # Remaining queue in order of arrival



#****************列表推导式*****************
vec = [2, 4, 6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])
freshfruit=['    banana','     loganberry','passion fruit    ']
print([weapon.strip() for weapon in freshfruit])
print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([[vec1[i]*vec2[i] for i in range(len(vec1))]])
print(list(range(1,6)))


# ***************嵌套列表解析*************
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print([[row[i] for row in matrix] for i in range(4)])

#del 语句
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
# 这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
# 或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

#元组和序列
# 元组由若干逗号分隔的值组成
t=12345,54321,'hello!'
print(t[0])
print(t)
u=t,(1,2,3,4,5)
print(u)
# 元组在输出时总是有括号的，以便于正确表达嵌套结构。
# 在输入时可能有或没有括号， 
# 不过括号通常是必须的（如果元组是更大的表达式的一部分）。


# 集合：是一个无序不重复元素的集。
# 可以用大括号({})创建集合。注意：如果要创建一个空集合，
# 你必须用 set() 而不是 {} ；后者创建一个空的字典
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)#删除重复的
print('orange'in basket)
print('crabgrass'in basket)
a=set('abracadabra')
b=set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

# 集合也支持推导式
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)


# 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)


print(dict([('sape',4139),('guido',4127),('jack',4096)]))
print({x:x**2 for x in(2,4,6)})
print(dict(sape=4139, guido=4127, jack=4098))


#字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions=['name','quest','favourate color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(q,a))
for i in reversed(range(1,10,2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)