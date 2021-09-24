# from os import write

# f=open("main.txt",'r')
# k=f.readlines()
# for i in k:
#     if "delhi" in i:
#         b=open("maindelhi.txt","a")
#         b.write (i)
#         print(b)
#     elif "shimla" in i:
#         p=open("mainshimla.txt","a")
#         p.write(i)
#         print(p)
#     else:
#         s=open("mainothers.txt","a")
#         s.write(i)
#         print(s)

# k=open("main.txt","r")8
# s="my name is rajitha"
# i=0
# c=0
# while i<len(s):
#     print(s[i],end="")
#     c=c+1
#     i+=1
# print(c)    
# k.close()


# k=open("main.txt","r")
# s=k.read()
# i=0
# c=0
# while i<len(s):
#     if s[i]!=" ":
#         c=c+1
#     i+=1
# print(c)
# k.close()


# k=open("main.txt","r+")
# s=k.read()

# l=k.write("im am raji")
# print(s)
# k.close()





# k=open("ashu.txt","a")

k=open("main.txt","r")
s=k.read()
a=s.split()
i=0
while i<len(a):
    # if i==3:
    #     print(a[i])
    # i=i+1
    if a[i]=='raji':
        print(a[i])
    i=i+1
    





