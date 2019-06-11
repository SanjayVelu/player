stng1,stng2=map(str,input().split())
c=0
for i in range(len(stng1)):
    if stng[i]!=stng2[i]:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
