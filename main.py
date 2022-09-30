func = lambda x, y: func(x + [y], input('write lines, to stop write: "stop" ')) if y != 'stop' else x
new_lines = func([], input('write lines, to stop write: "stop" '))

print(new_lines)
if new_lines:
	with open('data.txt', 'w') as f:
		for line in new_lines:
			f.write(line + '\n')
else:
	print('data was preserved')
