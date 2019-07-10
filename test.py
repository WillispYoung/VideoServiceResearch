import sys

file1 = open('cdns1.txt', 'r')
file2 = open('cdns2.txt', 'r')
output = open('cdns-out.txt', 'w')

s1 = set([l.strip() for l in file1.readlines()])
s2 = set([l.strip() for l in file2.readlines()])

res = s1.union(s2)
for s in res:
	output.write(s + "\n")

output.close()
