def check(arr1, arr2, n):
    set1 = list(set(arr1))
    set2 = list(set(arr2))

    if len(set1) !=n or len(set2) != n:
        return False
    
    set3 = [i for i in set1 if i in set2]
    
    if len(set3) == n:
        return True
    else:
        return False