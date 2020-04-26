user_input = input()
text_list = [char for char in user_input]
iteration_num = len(text_list)

answer = []
for i in range(iteration_num):
	if i % 2 == 0:
		string_parsed = text_list.pop(0)
		answer.append(string_parsed)
	else:
		string_parsed = text_list.pop(-1)
		answer.append(string_parsed)
		
print("".join(answer))