# def gen_num():
# 	print("첫 번째 실행")
# 	yield 1
# 	print("두 번째 실행")
# 	yield 2
#
# gen=gen_num()  #gen_num()의 객체 생성
# print(next(gen))
# print(next(gen))
#
# def gen_for():
# 	for i in list(range(1,10+1)):
# 		print(f"{i}번째 값:{i}")
# 		yield i
# gen=gen_for()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

import sys

def pow(s):
	li=[]
	for i in s:
		li.append(i**2)
	return li
st=pow(list(range(1,4+1)))
for i in st:
	print(i,end=" ")

print()

print(sys.getsizeof(st))
print()

def gen_pow(s):
	for i in s:
		yield i**2
st=gen_pow(list(range(1,4+1)))
for i in st:
	print(i,end=" ")
	print(type(i))
print()

print(sys.getsizeof(st))

print(type(st))