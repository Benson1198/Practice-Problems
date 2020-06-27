def ispar(s):
    par = []
    sqr = []
    cur = []
    
    lst = list(s)
    
    for i in lst:
        if i in '[({':
            if i == '[':
                sqr.append('[')
            elif i == '(':
                par.append('(') 
            elif i == '{':
                cur.append('{')
        else:
            if i == ']':
                if len(sqr) == 0:
                    return False
                else:
                    sqr.pop()
            elif i == ')':
                if len(par) == 0:
                    return False
                else:
                    par.pop()
            elif i == '}':
                if len(cur) == 0:
                    return False
                else:
                    cur.pop()
                    
    if len(sqr) == len(par) and len(par) == len(cur) and len(cur) == 0:
        return True