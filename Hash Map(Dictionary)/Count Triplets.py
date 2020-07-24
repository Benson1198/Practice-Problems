# Kind of Brute Force but still Dimag laga isme LOL
def countTriplets(arr, r):
    max_ele = max(arr)
    min_ele = min(arr)

    count = 0

    mul_arr = []
    div_arr = []

    for i in arr:
        mul = i*r
        div = int(i/r)

        if mul > max_ele:
            mul_arr.append(False)
        elif mul <= max_ele:
            mul_arr.append(mul)
        
        if div < min_ele:
            div_arr.append(False)
        elif div >= min_ele:
            div_arr.append(div)

    for i in range(n-1):
        for j in range(i+1,n-1):
            if mul_arr[i] == arr[j]:
                for k in range(j+1,n):
                    if arr[j] == div_arr[k]:
                        count += 1

    return count


# Optimised Method

def countTriplets(arr, r):
    a = Counter(arr)
    b = Counter()
    s = 0
    for i in arr:
        j = i//r
        k = i*r
        a[i]-=1
        if b[j] and a[k] and not i%r:
            s+=b[j]*a[k]
        b[i]+=1
    return s