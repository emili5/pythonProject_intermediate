#10이하의 자연수 중 3의배수만 리스트에 담는 코드

st=list(filter(lambda n:not(n%3),[1,2,3,4,5,6,7,8,9,10]))
print(st)

st=list(filter(lambda n:n%2,range(1,10+1)))
print(st)

#map과 filter
#map함수의 반환값에서 filter함수를 사용하여 특정 조건을 만족하는 iterator객체를 만들기
#1부터 20까지 숫자 중 4의 배수의 제곱값 구하기
st=filter(lambda n:not(n%4),map(lambda n:n**2,range(1,20+1)))
for i in st:
	print(i,end=" ")
print()


# 1부터 10까지 숫자 중 2의 배수의 제곱값 구하기
st=map(lambda n:n**2,filter(lambda n:not(n%2),range(1,10+1)))
for i in st:
    print(i,end=" ")
