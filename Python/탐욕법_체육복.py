import numpy as np

def solution(n, lost, reserve):
	arr = np.array([1] * n)
	lost_idx = np.array(lost) - 1
	reserve_idx = np.array(reserve) - 1

	arr[lost_idx] -= 1
	arr[reserve_idx] += 1

	try:
		if arr[0] == 0 and arr[1] > 1:
			arr[0] += 1
			arr[1] -= 1

		for i, val in enumerate(arr[1:]):
			if val == 0 and arr[i] >=2:
				arr[i + 1] += 1
				arr[i] -= 1
			elif val == 0 and arr[i + 2] >= 2:
				arr[i + 1] += 1
				arr[i + 2] -= 1
	except:
		pass
	
	answer = sum(arr >= 1)
	return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

answer = solution(n, lost, reserve)
print(answer)