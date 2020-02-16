# solution 1
def solution(citations):
    if sum(citations) == 0:
        return 0
    else:
        for h in range(max(citations), 0, -1):
            over_h = 0
            for citation in citations:
                if citation >= h:
                    over_h += 1
                if over_h == h:
                    return h

#################################################
# solution 2 
# test case 11 X

import numpy as np

def solution(citations):
    # citations = sorted(citations, reverse=True)
    
    for num in reversed(range(len(citations))):
        doc = sum(np.array(citations) >= num) 
        print(doc)
        if doc >= num:
            return num