import os
import sys

location = ["hongkong", "singapore"]
date = ["19-7-8", "19-7-9", "19-7-10", "19-7-11", "19-7-12"]
website = ["youtube"]


for l in location:
	print(l)

	cdn_complete_set = set()
	for d in date:
		for w in website:
			path = "data/" + l + "/" + d + "/" + w + "/cdns.txt"
			if os.path.exists(path):
				for line in open(path, 'r').readlines():
					domain = line.strip()
					if len(domain):
						cdn_complete_set.add(domain)
	
	print("total: " + str(len(cdn_complete_set)))
	size_of_complete_set = len(cdn_complete_set)

	for d in date:
		for w in website:
			path = "data/" + l + "/" + d + "/" + w + "/cdns.txt"
			if os.path.exists(path):
				size = len(set(open(path, 'r').readlines()))
				# print(size)
				print(d + "\t" + str(size / size_of_complete_set))

	print()
