x=3.2
print(type(x))
print(x.is_integer())   #is_integer()은 실수가 정수이면 True반환 실수가 실수이면 False반환

# 함수도 클래스
def func1(n):
    return n
def func2():
    print("This is func2")
print(type(func1))
print(type(func2))

#함수도 객체로써 함수의 매개변수로
def say1():
    print("hi")
def say2():
    print("Hello")
def caller(fct):
    fct()

caller(say1)
caller(say2)

#함수를 반환
def fct_fac(n):
    def exp(x):
        return x**n
    return exp
f3=fct_fac(3)   #f3는 x**3 계산 후 반환하는 함수 참조
f4=fct_fac(4)   #f4는 x**4 계산 후 반환하는 함수 참조
print(f3(2))
print(f4(3))

#람다식으로 표현
def fct_fac(n):
    return lambda x:x**n
f3=fct_fac(3)   #f3는 x**3 계산 후 반환하는 함수 참조
f4=fct_fac(4)   #f4는 x**4 계산 후 반환하는 함수 참조
print(f3(2))
print(f4(3))