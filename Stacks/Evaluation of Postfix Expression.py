def EvaluatePostfix(exp):
    lst = []
    inp = list(str(exp))
    
    ops = '+-*/'
    
    for i in inp:
        if i not in ops:
            lst.append(int(i))
        else:
            b = lst.pop()
            a = lst.pop()
            if i == '+':
                lst.append((a+b))
            elif i == '-':
                lst.append((a-b))
            elif i == '*':
                lst.append((a*b))
            elif i == '/':
                lst.append((a/b))
    return lst[0]