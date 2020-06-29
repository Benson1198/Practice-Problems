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