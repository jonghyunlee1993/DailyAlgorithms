def solution(s):
    s = s.split(" ")
    for i, word in enumerate(s):
        try:
            word = word[0].upper() + word[1:].lower()
        except:
            word.lower()
        s[i] = word
    
    return " ".join(s)