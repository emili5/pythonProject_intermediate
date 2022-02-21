from collections import namedtuple

# namedtuple 클래스의 이름은 man이고 튜플의 요소로 아래 4개의 이름을 가진 요소를 갖는다는 정보를 info라는 변수에 저장
info = namedtuple("man",['name','height','age','hobby'])

#새로운 객체 생성 및 참조
# manA라는 객체변수가 namedtuple객체 정보를 담은 info를 참조
manA = info("Alice",176.4,32,'running')
manB = info('Bob',187.2,23,'playng the piano')
print(f"manA의 정보 : 이름-{manA.name} 키-{manA.height} 나이-{manA.age} 취미-{manA.hobby}")
print(f"manB의 정보 : 이름-{manB.name} 키-{manB.height} 나이-{manB.age} 취미-{manB.hobby}")

print(f"manA의 정보 : 이름-{manA[0]} 키-{manA[1]} 나이-{manA[2]} 취미-{manA[3]}")

# 네임드 튜플의 패킹과 언패킹
A,*B=manA
print(A)
print(B)

# 함수의 매개변수에서 *은 언패킹
def desc(a,b,c,d):
    print(a,b,c,d)
e=manA
desc(*e)
