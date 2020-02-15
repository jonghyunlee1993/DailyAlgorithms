import string

def jacade(set1, set2):
    intersection = []
    union = []
    
    if len(set1) >= len(set2):
        for v1 in set2:
            if v1 in set1:
                intersection.append(v1)
        union = set1 + set2 
        for l1 in intersection:
            if l1 in union:
                union.remove(l1)  
    else:
        for v2 in set1:
            if v2 in set2:
                intersection.append(v2)
        union = set1 + set2
        for l2 in intersection:
            if l2 in union:
                union.remove(l2)
                
    return len(intersection) / len(union)
                
def solution(str1, str2):
    str1_list = []
    str2_list = []
    # punc = string.punctuation + string.whitespace + "0123456789"
    # for p in punc:
    #     str1 = str1.replace(p, "")
    #     str2 = str2.replace(p, "")
    
    alphabet = string.ascii_lowercase
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        if str1[i] in alphabet and str1[i+1] in alphabet:
            str1_list.append(str1[i] + str1[i+1])
            
    for j in range(len(str2)-1):
        if str2[j] in alphabet and str2[j+1] in alphabet:
            str2_list.append(str2[j] + str2[j+1])
    
    try:
        j = jacade(str1_list, str2_list)
        return int(j * 65536)
    except:
        return 65536
    
    