def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    for idx, i in enumerate(phone_book):
        i_length = len(i)
        for j in phone_book[idx+1:]:
            if i == j[:i_length]:
                return False
    return True