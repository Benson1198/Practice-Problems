def stockSpan(arr):
    n = len(arr)

    stack = []

    v = []

    for i in range(0,n):
        if len(stack) == 0:
            v.append(-1)
        elif len(stack) > 0 and arr[i] < stack[-1][0]:
            v.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] <= arr[i]:

            while len(stack) > 0 and stack[-1][0] <= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                v.append(-1)
            else:
                v.append(stack[-1][1])
        
        stack.append([arr[i],i])

    for i in range(n):
        v[i] = abs(v[i] - i)

    
    return v