def nextSmallerElementToLeft(arr):
    n = len(arr)

    stack = []

    v = []

    for i in range(0,n):
        if len(stack) == 0:
            v.append(-1)
        elif len(stack) > 0 and arr[i] > stack[-1]:
            v.append(stack[-1])
        elif len(stack) > 0 and stack[-1] >= arr[i]:

            while len(stack) > 0 and stack[-1] >= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                v.append(-1)
            else:
                v.append(stack[-1])
        
        stack.append(arr[i])
    
    return v





def nextSmallerElementToLeft(arr):
    n = len(arr)

    stack = []

    v = []

    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            v.append(-1)
        elif len(stack) > 0 and arr[i] > stack[-1]:
            v.append(stack[-1])
        elif len(stack) > 0 and stack[-1] >= arr[i]:

            while len(stack) > 0 and stack[-1] >= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                v.append(-1)
            else:
                v.append(stack[-1])
        
        stack.append(arr[i])

    v.reverse()
    
    return v


