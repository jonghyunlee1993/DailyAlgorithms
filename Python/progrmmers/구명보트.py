# 올바른 풀이
def solution(people, limit):
    boat = 0
    people.sort()
    
    i = 0
    j = len(people) - 1
    
    while i <= j:
        boat += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    
    return boat

# 처음에 잘못 생각함
def solution(people, limit):
    boat = 1
    on_board = 0
    people = sorted(people, reverse=False)
    
    while people:
        person = people.pop(0)
        if on_board + person <= limit:
            on_board += person
        else:a
            boat += 1
            on_board = person

    return boat