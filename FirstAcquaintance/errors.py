while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")
    except (RuntimeError, TypeError, NameError):
        pass


import sys

try:
    f = open('myfile.txt','r+')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# 可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
# 这个子句将在try子句没有发生任何异常的时候执行

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise  #并不想去处理它，简单的 raise 语句就可以再次把它抛出。


# 用户自定义异常
class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:',e.value)


# 定义清理行为
# try 语句还有另外一个可选的子句 finally，
# 它定义了无论在任何情况下都会执行的清理行为。
# 不管 try 子句里面有没有发生异常，finally 子句都会执行。

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
# 而又没有任何的 except 把它截住，
# 那么这个异常会在 finally 子句执行后再次被抛出。

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
# divide("2", "1")


# **************预定义的清理行为***********
# 关键词 with 语句就可以保证诸如文件之类的对象
# 在使用完之后一定会正确的执行他的清理方法:

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

