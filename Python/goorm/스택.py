num_inputs = int(input())
iteration = 0
stack = []

while iteration < num_inputs:
	iteration += 1
	condition = int(input())
  # push
	if condition == 0:
		if len(stack) <= 10:
			item = int(input())
			stack.append(item)
		elif len(stack) > 10:
			print("overflow")
	# pop
	elif condition == 1:
		# item이 있을 때
		if stack:
			stack.pop(-1)
		# item이 없을 때
		elif not stack:
			print("underflow")
	else:
		break
		
if len(stack) > 1:
	str_stack = list(map(str, stack))
	print(" ".join(str_stack) + " ")
elif len(stack) == 1:
	print(stack[0])