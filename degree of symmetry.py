def sym(string,length, deg=0):
    if length==1:
        return deg
    elif string[0:int(length/2):1]==string[int(length/2):int(length):1]:
        return sym(string[0:int(length/2):1],length/2,deg+1)
    else: return deg
length=int(input("Enter length of string \n"))
string=str(input("Enter string \n"))
print(str(sym(string,length)))
