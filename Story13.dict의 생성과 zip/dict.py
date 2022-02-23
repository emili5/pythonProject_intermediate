#dict을 만드는 다양한 방법

#1. 직접 형태를 만들어주기
a={'a':1,'b':2,'c':3}
print(a)

#2. dict()함수에 전달하여 반환하기

b = dict(a=1,b=2,c=3)
print(b)
c =dict([('a',1),('b',2),('c',3)])
print(c)
d= dict((['a',1],['b',2],['c',3]))
print(d)
g = dict(['a','b','c'],(1,2,3))
print(g)
# zip()함수를 이용하여 만들기
e = dict(zip(['a','b','c'],[1,2,3]))
print(e)
f = dict(zip(('a','b','c'),(1,2,3)))
print(f)