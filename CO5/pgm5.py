# .write a python program to write a Python dictionary to a csv file.afterwriting the csv file read the csv file and display the content

import csv
import pandas
field=['name','rollno','age']
sdict=[{'name':'amal','rollno':9,'age':22}, {'name':'anurag','rollno':16,'age':29}]
with open("dpt.csv","w") as dfile:
 writer=csv.DictWriter(dfile,fieldnames=field)
writer.writeheader()
writer.writerows(sdict)
data=pandas.read_csv("dpt.csv")
print(data)