def swapCase(s):
    w=[]
    for l in s:
        if(l.isupper()):
            w.append(l.lower()) 
        elif(l.islower()):
            w.append(l.upper())
        else:
            w.append(l)    
    return "".join(w)   
 
s="teK leys MN12 3" 
print(swapCase(s))