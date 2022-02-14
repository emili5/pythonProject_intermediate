#리스트 컴프리헨션으로 만든 리스트 객체를 매개변수로 전달
def show_all(s):
	for i in s:
		print(i,end=" ")
st=[2*i for i in range(1,10)]  #리스트 컴프리헨션 사용
show_all(st)

print()


def show_all(s):
	for i in s:
		print(i,end=" ")

#제너레이터 함수로 만든 제너레이터 객체를 매개변수로 전달
def gshow_all():
	for i in range(1,10):
			yield 2*i
g=gshow_all()
show_all(g)

print()

# 제너레이터 표현식으로 만든 제너레이터 객체를 매개변수로 전달
a=(2*i for i in range(1,10))
#show_all(a)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(next((2*i for i in range(1,10))))
print(next(2*i for i in range(1,10)))



