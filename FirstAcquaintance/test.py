#!usr/bin/python3
#Filename:test.py
from fibo import fib,fib2
import support
# from fibo import *   这种声明不该被过多地使用。

support.print_func("RUNoob")
print_func=support.print_func
print_func("RUNoob2")

fib(100)


print(dir())