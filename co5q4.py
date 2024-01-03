import csv
field=['rollno','name','age']
sdict=[{'rollno':10,'name':'ALshin','age':21},
       {'rollno':11,'name':'aby','age':18},
       {'rollno':12,'name':'eby','age':10}]
with open("ppt.csv",'w') as dfile:
       writer=csv.DictWriter(dfile,fieldnames=field)
       writer.writeheader()
       writer.writerows(sdict)    
      

