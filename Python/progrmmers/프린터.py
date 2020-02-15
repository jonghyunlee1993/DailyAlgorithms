import numpy as np

def solution(priorities, location):
    count = 0
    
    my_doc = [False] * len(priorities)
    my_doc[location] = True
    
    while True:
        doc = priorities.pop(0)
        is_my_doc = my_doc.pop(0)
        is_higher = sum(np.array(priorities) > doc)
        
        if is_higher:
            priorities.append(doc)
            my_doc.append(is_my_doc)
        elif not is_my_doc and not is_higher:
            count += 1
        elif is_my_doc and not is_higher:
            count += 1
            return count