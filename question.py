f=open("question.txt")
lines=f.readlines()
i=0
c=0
while i<len(lines):
    print(lines[i],end="")
    c=c+1
    i+=1
print(",","how many lines",c)    


