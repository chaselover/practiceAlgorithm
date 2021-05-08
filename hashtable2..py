# 순열

def permute(arr): 
    result = [arr[:]] 
    c = [0] * len(arr) 
    i = 0 
    while i < len(arr):
        if c[i] < i: 
            if i % 2 == 0: 
                arr[0], arr[i] = arr[i], arr[0] 
            else: 
                arr[c[i]], arr[i] = arr[i], arr[c[i]] 
                
            result.append(arr[:]) 
            c[i] += 1
            i = 0 
        else: 
            c[i] = 0 
            i += 1 
            return result


def perm(lis, n): result = [] if n > len(lis): return result if n == 1: for li in lis: result.append([li]) elif n > 1: for i in range(len(lis)): tmp = [i for i in lis] tmp.remove(lis[i]) for j in perm(tmp, n-1): result.append([lis[i]]+j) return result n = int(input()) lis = list(i for i in range(1, n+1)) for li in perm(lis,n): print(' '.join(list(map(str, li))))

