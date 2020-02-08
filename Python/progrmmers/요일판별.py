import datetime

def solution(a, b):
    dow = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    date = datetime.datetime(2016, int(a), int(b))
    answer = date.weekday()
    return dow[answer]