# A의 가장 작은 값과 B의 가장 큰 값을 곱해서 더한다
def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    res = 0
    for i in range(len(A)):
        res += A[i] * B[i]
    
    return res

def solution(A,B):
    product_res = [0] * len(A)
    
    for iteration in range(len(A)):
        res = 0
        for i in range(len(A)):
            res += A[i] * B[i]
        
        product_res[iteration] = res
        B.append(B.pop(0))
    
    return min(product_res)
        