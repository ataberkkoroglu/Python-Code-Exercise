liste=[(3,4),(10,3),(5,6),(1,9)]
liste2=[]
liste3=[]
for i,e in liste:
    liste2.append(i)
    liste3.append(e)
print(list(map(lambda x,y:x*y,liste2,liste3)))
