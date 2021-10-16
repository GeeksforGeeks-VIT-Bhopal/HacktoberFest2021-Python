import re
t = int(input())
for i in range(0,t):
    x = input()
    if(x.count("-")>0):
        a = x.split("-")
        p=1
        if(len(a)!=4):
            p=None
            a=[]
        for b in a:
            if len(b)!=4:
                p=None
                break
    else:
        p=re.search("[456][0-9]{15}",x)
    x=x.replace("-","")
    q= re.search(".*([0-9])\\1{3}.*",x)
    if(p!=None and q==None):
        print("Valid")
    else:
        print("Invalid")