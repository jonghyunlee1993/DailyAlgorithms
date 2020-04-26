array_size = int(input())
num_list   = list(map(int, input().replace(" ", "")))
target     = int(input())

def binary_search(array_size, num_list, target):
	start = 0
	end = array_size - 1

	while start <= end:
			mid = (start + end) // 2

			if num_list[mid] == target:
					return print(mid + 1)
			elif num_list[mid] < target:
					start = mid + 1
			else:
					end = mid -1

	return print("X")

binary_search(array_size, num_list, target)