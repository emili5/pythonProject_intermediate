r1=list(range(1,11))
r2=[i**2 for i in r1]
print(r2)

r1=[1,2,3,4,5]
r2=[i**2 for i in r1 if i%2==0]
print(r2)

r1=[1,2,3]
r2=[1,2,3]
r3=[int(str(i)+str(j)) for i in r1 for j in r2]
print(r3)

#조건이 들어간 이중 for문
r=[n*m for n in range(2,9+1) for m in range(1,9+1) if n*m%2==0]
print(r)