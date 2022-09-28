new_line = input('u may add some new lines in your data if you wish')

with f as open('data.txt'):
	data = [line.split(',') for line in f]
	for row in data:
		print(f'name: {data[0]}, surname: {data[1]}, age: {data[3]}, salary: {data[-1]}')
	f.write(data + new_line)

	