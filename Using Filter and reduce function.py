from functools import reduce

a=list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10]))
print(a)
if a==[2,4,6,8,10]:
    print(reduce(lambda x,y:x+y,a))
