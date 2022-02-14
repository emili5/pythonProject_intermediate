#튜플 패킹
a=1,2
b=(1,2)
print(type(a))
print(type(b))
print(a)
print(b)

#튜플 언패킹
c=('a','b')
a,b=c
print(a,b)

#튜플 언패킹에서 하나의 변수에 리스트 저장
tp=1,2,3,4,5,6
a,b,*c=tp
print(a)
print(b)
print(c)
print(type(a))
print(type(c))

#반환값으로 변수에 튜플 생성하기
def ret_nums():
	return 5,6,7,8
a=ret_nums()
print(a)

a,b,*c=ret_nums()
print(c)

#매개변수로 튜플을 받는 예제1
def ab(a,b,*c):
    return c
a=ab(3,4,5,6,7)
print(a)

#매개변수로 튜플을 받는 예제2
def nums(*num):
	for i in num:
		print(i,end=" ")
nums(9,8,7,6,5)

print()

#함수 호출에서 *는 튜플 언패킹 의미
def info(a,b,c):
	print(a,b,c)

tp='A','B','C'
info(*tp)

tp=(1,2,3,(5,6))
a,b,c,(d,e)=tp
print(d)

# 불필요한 변수는 _로~
info=('안정민','B형',('배드민턴','탁구'))
#name,bloodType,(hb1,hb2)=info
_,_,(hb1,hb2)=info
print('취미는',hb1,hb2)

#for문으로 튜플, 리스트 형식의 변수를 다른 변수에 저장하기
info=(('A',1),('B',2),('D',76))
for (i,j) in info:
	print(f"{i}의 값은 {j}")

info=(['pencil','cup'],['food','water'],['money','gold'])
for [i,j] in info:
	print(f"{i}의 짝꿍은 {j}!")