#map함수의 반환값은 iterator객체이다
def pow(a):
	return a
str='sweet' #String'과 int자료형은 operator안됨!
itr=map(pow,str)
for i in itr:
    print(i, end=" ")

# def sum(a,b):
# 	return a+b
# st1=[1,2,3]
# st2=[3,2,1]
# result=list(map(sum,st1,st2))
# print(result)
#
# def rev(s):
# 	return s[ : : -1]
# rst=['one','two','three']
# result=list(map(rev,rst))
# print(result)



