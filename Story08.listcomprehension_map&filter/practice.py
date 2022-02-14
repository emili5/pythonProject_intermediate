st=list(filter(lambda n: not(n%3),[1,2,3,4,5,6,7,8,9,10]))  #not(n%3) -> 1(True)
print(st)

st=[i for i in range(1,10+1) if i%3==0]
print(st)

#1부터 20까지 숫자 중 4의 배수의 제곱값 구하기
st=list(filter(lambda n:not(n%4),map(lambda n:n**2,range(1,20+1))))
print(st)

st=[i**2 for i in range(1,20+1) if i%2==0]
print(st)