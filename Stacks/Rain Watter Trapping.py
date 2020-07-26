def rainWaterTrapped(arr):
    n = len(arr)
    left_arr = [arr[0]]
    right_arr = [0]*(n-1)
    right_arr.append(arr[-1])

    area = 0

    for i in range(1,n):
        left_arr.append(max(arr[i],left_arr[i-1]))

    for i in range(n-2,-1,-1):
        right_arr[i]  = max(arr[i],right_arr[i+1])

    for i in range(n):
        temp_max = min(left_arr[i],right_arr[i])
        if temp_max >= arr[i]:
            area += (temp_max - arr[i])

    return area
    
print(rainWaterTrapped([3,0,0,2,0,4]))