import sys

a = 0
b = 300
n=33            #position index inside ordered result list
a += 1
global myres
myres=[]
for i in range(a,b):
    y = True
    if(str(i) == str(i)[::-1]):
        if(i>2):
            for a in range(2,i):
                if(i%a==0):
                    y = False
                    break
            if y:
                #myres=myres + ', ' + str(i)
                myres.append(i)
    if(len(myres)==n):
        break
print (myres)

# to do a element-wide operation (xor) on two lists
#   [x^y for x,y in zip(a,b)]
# from int to ASCII
#   for ch in c:
#       print(chr(ch))