#iter() & next()
# list=list(range(1,5))
# print(list)
# ir=iter(list)
# print(ir)
# print(next(ir))
# print(next(ir))
# print(next(ir))
# print(next(ir))
# print(next(ir))

# iterable한 객체 확인
tuple=(1,2,3)
ir=tuple.__iter__()     #ir=tuple.iter()
print(ir.__next__())    #next(ir)
print(ir.__next__())
print(ir.__next__())

#iterable한 객체인지 확인하는 방법 -dir()
t='HelloKitty'
print(dir(t))

#hasattr()
print(hasattr(t,'__iter__'))

#for문과 iterator
li=[i for i in range(1,10) if i%3==0]
ir=iter(li)
while True:
    try:
        i=next(ir)
        print(i,end=" ")
    except StopIteration:
        break