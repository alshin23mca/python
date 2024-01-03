l1=[2,1,3,5,6,7,2]
print("List1: ",l1)
l2=[]
for i in l1:
	if l1.count(i)>1:
		continue
l2.append(i)
print(l1)
print("deleted item: ",l2)


