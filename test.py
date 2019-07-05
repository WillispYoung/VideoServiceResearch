data = []
for line in open('urls.txt', 'r').readlines():
	if line.startswith('https://www.youtube.com/watch'):
		data.append(line)

output = open('urls.txt', 'w')
for d in data:
	output.write(d)
output.close()
