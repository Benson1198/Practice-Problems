def sherlockAndAnagrams(s):
    ctr=0
    for i in range(1,len(s)):
        for j in range(0,len(s)-i):
            ts1=sorted(s[j:i+j])
            for k in range(j+1,len(s)-i+1):
                if ts1==sorted(s[k:k+i]):
                    ctr+=1
    return ctr


    
