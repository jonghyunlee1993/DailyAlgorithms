import numpy as np

def calcCorrect(person, answers):
    answers = np.array(answers) 
    number = len(answers)
    
    mul = (number // 5) + 1
    
    data = np.array(person * mul)
    res = sum(answers == data[:number])
    
    return res
    
def compRes(data):
    idx = np.where(data == data.max())[0] + 1
    return idx.tolist()
    
def solution(answers):
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1]    
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5 ,5]
    
    A_res = calcCorrect(A, answers)
    B_res = calcCorrect(B, answers)
    C_res = calcCorrect(C, answers)
    
    holder = np.array([A_res, B_res, C_res])

    answer = compRes(holder)
    return answer

answers = [3,3,1,1,2,1,2,3,4,5,1,]
ans = solution(answers)
print(ans)