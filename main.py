new_line = input('u may add some new lines in your data if you wish')

with open('data.txt', 'r+') as f:
	data = [line.split(',') for line in f]

	for row in data:
		print(f'name: {row[0]}, surname: {row[1]}, age: {row[2]}, salary: {row[-1]}')

	if new_line:
		f.write('\n' + new_line)

	