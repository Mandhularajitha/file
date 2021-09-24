
# from os import write


my_file3 = open("q3.txt", "w")
l=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(l):
    my_file3.write(l[i])
    my_file3 .write("\n")
    i+=1
my_file3.close()
    
