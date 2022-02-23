# dict의 값에 접근하기 위한 다양한 방법

# 1.dict에서 키를 통해 값에 접근하기
di = dict(a=1,b=2,c=3)
for i in di:
    print(f"키:{i}",end=" ")
    print(f"값:{di[i]}")

# 2.dict의 keys(), values(), items() 함수-> 뷰 객체
di = dict(a=1,b=2,c=3)
for i in di.keys():
    print(i)
for i in di.values():
    print(i)
for i in di.items():
    print(i)

for a,b in di.items():
    print(a,b,sep=",")

# 뷰 객체는 딕셔너리의 현재 상태를 반영한다.
d = dict(a=1,e=4,o=b)
it=d.items()
for i in it:
    print(i)
print(d['e'])
d['e']+=3
for i in it:
    print(i)