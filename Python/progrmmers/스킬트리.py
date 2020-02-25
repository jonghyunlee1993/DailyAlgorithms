# 앞선 스킬을 배우는 제약이 있음

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        a = [tree.index(s) for s in skill if s in tree]
        a_ = sorted(a)
        
        if a == a_ and all(s in tree for s in skill[:len(a)]): answer += 1
    
    return answer


# 본 풀이는 앞선 스킬에 대한 제약을 고려하지 못함

def solution(skill, skill_trees):
    index = str()
    answer = 0

    for tree in skill_trees:
        for s in skill:
            try:
                index += str(tree.index(s))
            except:
                pass
        
        if index == ''.join(sorted(index)):
            answer += 1
        
        index = str()
        
    return answer