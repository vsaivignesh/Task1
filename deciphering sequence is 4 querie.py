x=0
y=5
i=0
reqd=[0,0,0,0,0,0]
arr=[7,43,10,9,16,8]
for j in range(2):
    enq1=int(input(str(x)+" "+str(y)))
    enq2=int(input((str(x+1)+" "+str(y))))
    while(reqd[x]==0 or reqd[y]==0):
        if(enq1%arr[i]==0):
            if(enq2%arr[i]==0):
                reqd[y]=arr[i]
                reqd[x+1]=enq2/arr[i]
                reqd[x]=enq1/arr[i]
            else:
                reqd[x]=arr[i]
                reqd[y]=enq1/arr[i]
                reqd[x+1]=enq2/reqd[y]
        i=i+1
    x=x+2
    y=y-1
    i=0
print(str(reqd))
