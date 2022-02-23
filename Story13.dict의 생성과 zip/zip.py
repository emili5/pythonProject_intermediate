# zip함수는 매개변수로 받은 iterable객체를 짝을 지어 튜플로 반환하는 함수
a =zip(['a','b','c'],[1,2,3])
for i in a:
    print(i)

#문자열,문자열 튜플
# b = zip('abc','123')
# for i in b:
#     print(i)

# 문자열,숫자 튜플
c=zip('abc',(1,2,3))
for i in c:
    print(i)

#문자열, 숫자 튜플
d = zip(['a','b','c'],[1,2,3])
for i in d:
    print(i)

#zip함수의 객체를 요소로 하는 딕셔너리 생성
e=dict(zip(['a','b','c'],[1,2,3]))
print(e)

#zip함수의 객체를 요소로 하는 리스트 생성
f =list(zip(('a','b','c'),(1,2,3)))
print(f)

# zip함수의 객체를 요소로 하는 튜플생성
g = tuple(zip(('a','b','c'),(1,2,3)))
print(g)

# zip함수로 셋 이상의 값들로 이루어진 객체 만들기
h = zip(['a','b','c'],[1,2,3],[10,20,30])
for i in h:
    print(i,end=" ")
