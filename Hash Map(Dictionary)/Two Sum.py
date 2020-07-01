# NOOB
def keypair(A, N, X):
     A.sort()
    
    for i in range(N):
        if A[i] >= X:
            return False
        else:
            diff = X-A[i]
            if diff in A[i+1:]:
                return True

# PRO
def keypair(A, N, X):
    
    s=dict()
    for i in range(0,N):
        temp=X-A[i]
        if(s.get(temp)):
            return True
        s[A[i]]=1
    return False