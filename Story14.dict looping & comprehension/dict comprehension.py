# 값을 3만큼 늘린 딕셔너리 만들기
di = dict(a=1,b=2,c=3,d=4,e=5,f=6)
print(di)

di2 = {k:v+3 for k,v in di.items()}
print(di2)

# 특정 조건을 가진 값을 가진 딕셔너리 만들기
di3= {k:v for k,v in di.items() if v%2==0}
print(di3)