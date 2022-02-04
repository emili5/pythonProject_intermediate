# immutable한 자료형인 튜플을 수정해보자
# a=(1,2,3)
# print(id(a))
# a+=(4,5)
# print(id(a))
# print(a)

#mutable한 객체를 인자로 넘긴 함수
a=[1,2,3]

def add_list(m,n):
    m+=n

add_list(a,[4,5])
print(a)

# immutable한 객체를 인자로 넘긴 함수
a=(1,2,3)
def add_tuple(m,n):
    m+=n
add_tuple(a, (4, 5))
print(a)

# immutable한 객체를 인자로 넘긴 함수-return
a=(1,2,3)
def add_tuple(m,n):
    m+=n
    return m
a=add_tuple(a, (4, 5))
print(a)
