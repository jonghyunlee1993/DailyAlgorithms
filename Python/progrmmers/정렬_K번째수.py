def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command

        my_arr = array[i-1:j]
        my_arr.sort()

        answer.extend([my_arr[k-1]])
        
    return answer