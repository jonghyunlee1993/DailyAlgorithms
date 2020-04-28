num_lines = int(input())

for iteration in range(1, num_lines + 1):
    answer = 0
    line = list(map(int, input().strip().split()))
    
    for number in line:
        if number % 2 == 1:
            answer += number
	
    print(f"#{iteration} {answer}")