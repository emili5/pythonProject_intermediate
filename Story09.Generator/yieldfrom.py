def pow(s):
    for i in s:
        yield i
st1=pow([1,2,3,4,5])
print(next(st1),end=" ")
print(next(st1),end=" ")
print(next(st1),end=" ")
print(next(st1),end=" ")
print(next(st1),end=" ")

print()
def pow(s):
    yield from s
st1=pow([1,2,3,4,5])
print(next(st1),end=" ")
print(next(st1),end=" ")
print(next(st1),end=" ")
print(next(st1),end=" ")
print(next(st1),end=" ")
