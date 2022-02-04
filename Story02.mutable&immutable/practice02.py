# mutable한 객체를 인자로 넘긴 함수
a=[14,1,3,6,7]
def max_list(m):
    m.sort()
    print(m[0],m[-1],sep=',')   #sep은 문자열이나 리스트 내에서 문자열을 구분하는 역할, 구분할 문자 지정가능
max_list(a)
print(a)

# mutable한 객체를 인자로 넘긴 함수-다른 참조 변수에 저장
a=[14,1,3,6,7]
def max_list(m):
    b=list(m)   #a의 내용이 담긴 새로운 리스트 생성
    b.sort()
    print(b[0],b[-1],sep=',')   #sep은 문자열이나 리스트 내에서 문자열을 구분하는 역할, 구분할 문자 지정가능
max_list(a)
print(a)

a=[2,1,5,9,2,8]
print(id(a))
b=a     # 같은 객체를 다른 변수도 참조하게 한 것임(같은 메모리 주소)
print(id(b))
c=list(a)   # 새로운 참조 변수가 새로운 주소의 리스트를 만들도록 하는 list()함수
print(id(c))
