import csv
with open("newQ.csv",'r') as efile:
  data=csv.reader(efile)
  for i in data:
     print(i)
