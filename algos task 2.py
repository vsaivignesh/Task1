def convtbin(a, ret=0):
    l=0
    while(int(a/(2**l))>0):
        l=l+1
    var=ret+(10**(l-1))
    a=a-2**(l-1)
    if (a==1) :
        return var+1
    elif (a==0):
        return var
    else:
        return convtbin(a, var)



length=int(input("Enter length"))
inp=str(input("Enter String"))
val=0
l=length-1
for i in range (0,length):
    val=val+(int(inp[i])*(2**l))
    l=l-1
if(val+1>=2**length or (val-1)<2**(length-1)):
    print(-1)
else:
    print(str(convtbin(val+1))+" "+str(convtbin(val-1)))
    



    
