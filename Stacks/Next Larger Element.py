# NOOB

def nextLargerElement(arr,n):
    res = [-1]*n
    
    for i in range(n):
        for j in range(i,n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    
    return res

# PRO

def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def nextLargerElement(arr,n):

    next_greater = [-1 for i in range(n)] 
    s = createStack()
    element = 0
    next = 0


    push(s, [arr[0],0])


    for i in range(1, n, 1):
        next = arr[i]

        if isEmpty(s) == False:


            elem = pop(s)
            element = elem[0]
            curr_index = elem[1]

            while element < next:
                next_greater[curr_index] = next 
                if isEmpty(s) == True:
                    break
                elem = pop(s)
                element = elem[0]
                curr_index = elem[1]

            if element > next:
                push(s, [element,curr_index])

        push(s, [next,i])
    
    return next_greater



# My Solution using STACKS

def nextLargerElementToRight(arr):
    n = len(arr)

    stack = []

    v = []

    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            v.append(-1)
        elif len(stack) > 0 and arr[i] < stack[-1]:
            v.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[i]:

            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                v.append(-1)
            else:
                v.append(stack[-1])
        
        stack.append(arr[i])

    v.reverse()
    
    return v

arr = [1,3,2,4]

print(nextLargerElementToRight(arr))