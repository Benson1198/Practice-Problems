def minimumSwapsToSort(arr):
    n = len(arr) 
    count = 0
    i = 0
      
    while i < n:
        if arr[i] != i + 1:
  
            while arr[i] != i + 1:
                arr[arr[i] - 1],arr[i] = arr[i],arr[arr[i] - 1]
                count += 1
        i += 1
    return count