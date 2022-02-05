# 리스트를 생성하는 다양한 방법
# 1. 리스트 형태로 선언
r1=[1,2,3]
r2=[]
r3=[[1,2,3],[4,5,6]]
print(r1)
print(r2)
print(r3)

#2. list()함수로 리스트 생성
r4=list((1,2,3))
r5=list()
r6=list('hello')
r7=list(range(0,10))
print(r4)
print(r5)
print(r6)
print(r7)

#3. 조건이 복잡한 리스트 만들기-for문
# 1~10까지 제곱 시킨 값을 가진 리스트
r1=list(range(1,11))
r2=[]
for i in r1:
    r2.append(i**2)
print(r2)

# 조건 필터 리스트 만들기-if문
r1=[1,2,3,4,5]
r2=[]
for i in r1:
    if i%2==0:
        r2.append(i**2)
print(r2)

#리스트의 모든 요소의 조합-이중 for문
r1=[1,2,3]
r2=[1,2,3]
r3=[]
for i in r1:
    for j in r2:
        r3.append(int(str(i)+str(j)))
print(r3)