def nearestSmallerLeft(arr):
    n = len(arr)

    stack = []
    pseudo_index = -1

    left = []

    for i in range(0,n):
        if len(stack) == 0:
            left.append(pseudo_index)
        elif len(stack) > 0 and arr[i] > stack[-1][0]:
            left.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] >= arr[i]:

            while len(stack) > 0 and stack[-1][0] >= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                left.append(pseudo_index)
            else:
                left.append(stack[-1][1])
        
        stack.append([arr[i],i])

    
    return left

def nearestSmallerRight(arr):
    n = len(arr)

    stack = []
    pseudo_index = len(arr)

    right = []

    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            right.append(pseudo_index)
        elif len(stack) > 0 and arr[i] > stack[-1][0]:
            right.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] >= arr[i]:

            while len(stack) > 0 and stack[-1][0] >= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                right.append(pseudo_index)
            else:
                right.append(stack[-1][1])
        
        stack.append([arr[i],i])

    right.reverse()
    
    return right

def maxAreaHistogram(arr):
    n = len(arr)

    left_arr = nearestSmallerLeft(arr)
    right_arr = nearestSmallerRight(arr)

    width_arr = []
    for i in range(n):
        width = abs(right_arr[i] - left_arr[i]) - 1
        width_arr.append(width)
        
    max_area = 0

    for i in range(n):
        temp_area = arr[i]*width_arr[i]
        if temp_area >= max_area:
            max_area = temp_area
    
    return max_area

print(maxAreaHistogram([6,2,5,4,5,1,6]))