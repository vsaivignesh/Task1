n,r,x,y=input("Enter first line").split()
org=int(r)
contest=list(map(int,input().split()))
scn=list(map(int,input().split()))
for i in range(len(contest)):
    if(contest[i]==1):
        if(scn[i]==1):
           r=int(r)+int(x)
        else:
            r=int(r)-int(y)
if(int(r)>org):
    print("Promoted")
elif(int(r)<org):
    print("Demoted")
else: print("No change")
