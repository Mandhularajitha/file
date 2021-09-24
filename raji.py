
f= open("q3.txt", "w")
l=[1,2,3,4,5]
for i in l:
    f.write(str(i))
    # print(l[i])
f.close()