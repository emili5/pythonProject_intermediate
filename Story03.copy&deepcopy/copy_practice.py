# 내용만 같은 서로 다른 객체를 참조하는 두 참조 변수 비교
r1=[1,2,3]
r2=[1,2,3]
print(r1==r2)
print(r1 is r2)

r1=[1,2,3]
r2=r1
print(r1==r2)
print(r1 is r2)


r1=['emili',('woman','Korea'),[170,21]]
r2=list(r1) # r1과 동일한 내용을 담는 r2라는 새로운 객체 생성
print(r1==r2)   # 두 객체의 내용이 같은지 비교

print(r1 is r2) # 두 객체가 동일한지 비교
print(r1[0] is r2[0])   # 두 객체의 첫 번째 요소가 동일한지 비교
print(r1[1] is r2[1])
print(r1[2] is r2[2])
