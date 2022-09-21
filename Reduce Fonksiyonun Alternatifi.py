from functools import reduce

#reduce function usage
result=reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10])
print(result)

#Alternative of Reduce Function
g=[1,2,3,4,5,6,7,8,9,10]
def function(g):
     total=0
     for i in range(0,10):
          total=total+(g[i])
          yield total
          

Generator=function(g)
Iteration=iter(Generator)
while(1):
     try:
      print(next(Iteration))
     except:
          break
