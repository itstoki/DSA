def longestCommonPrefix(strs):
    ans=[]
    ch=""
    if strs=="":
        return "".join(strs)
    if len(strs)==1:
        return "".join(strs)   
    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            if i >= len(strs[j]):
                return "".join(ans)
            if strs[0][i]==strs[j][i]:
                ch=strs[0][i]    
            elif(strs[0][i]!=strs[j][i]):
                return "".join(ans)   
        ans.append(ch)
    return "".join(ans)
s=["flower","flow","flight"] 
print(longestCommonPrefix(s))   