import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

urls1 = set(open(file1, "r").readlines())
urls2 = set(open(file2, "r").readlines())

urls = urls1.union(urls2)

writer = open("cdns_.txt", "w")
for url in urls:
	writer.write(url)
writer.close()

