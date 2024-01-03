#write odd lines of the file odd.txt 
#copy the even lines of the file to even.txt

stud=open("stud.txt",'r')
oddline=open("odd.txt",'w')
evenline=open("even.txt",'w')
content=stud.readlines
print("Contents of the files r: ")
print(content)

for i in range(len(content)):
    if(i%2==0):
      evenline.write(content[i])
    else:
      oddline.write(content[i]) 
stud.close()
evenline.close()
oddline.close()
oddline=open("stud.txt",'r')       
     
