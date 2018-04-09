def square(x):
    return x ** 2
A=map(square,[1,2,3,4,5])
print(list(A))

def numJewelsInStones(J, S):
    return sum(map(J.count, S))
def numJewelsInStones2(J, S):
    return sum(map(S.count, J))

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J,S))
print(numJewelsInStones2(J,S))
print(S.count(J))
def fahrenheit(T):
    '''返回华氏温度'''
    return ((float(9)/5)*T + 32)
def celsius(T):
    '''返回摄氏温度'''
    return (float(5)/9)*(T-32)
temperatures = (36.5, 37, 37.5, 38, 39)

F = list(map(fahrenheit, temperatures))
C = list(map(celsius, F))
print(F)
print(C)

C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
# [3, 7, 11, 15, 19]