import sys         # 引入 sys 模块


list1=[1,2,3,4]
it = iter(list1)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
print('\n')


 
list=[1,2,3,4,5]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()