#함수는 객체이므로 다른 참조 변수에 붙여서 또 함수로 이용가능
def show(s):
    print(s)
ref=show
ref("Hello")

#람다를 이용한 함수
ref=lambda s:print(s)
ref("Hello")

#매개변수가 여러 개 + 반환값이 있는 람다함수
f1=lambda n,m: n*m
print(f1(3,4))

f2=lambda s : len(s)
print(f2([1,2,3]))