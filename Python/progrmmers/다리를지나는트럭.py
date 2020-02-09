def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    sec = 0
    while True:
        try:
            queue.pop(0)
            if truck_weights:
                if sum(queue) + truck_weights[0] <= weight:
                    queue.append(truck_weights.pop(0))
                else:
                    queue.append(0)
            sec += 1
        except:
            return sec


if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]

    res = solution(bridge_length, weight, truck_weights)
    print(res)