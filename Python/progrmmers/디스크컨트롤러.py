# 시도중

def solution(jobs):
    jobs.sort(key = lambda element : element[0])
    time = 0
    total_duration = 0
    
    while True:
        job = jobs.pop(0)
        time += job[0]
        total_duration += job[1]
        
        if jobs[0][0] > time:
            obs.sort(key = lambda element : element[1])
        else:
            pass
        