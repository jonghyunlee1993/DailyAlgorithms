def solution(n):
    result = [0]
    count = 1
    
    if n == 1:
        return [0]
    else:
        while count != n:
            result_next = result.copy()
            result_next.append(0)

            for i in reversed(result):
                if i == 0:
                    result_next.append(1)
                else:
                    result_next.append(0)
            
            result = result_next
            count += 1
            
    return result