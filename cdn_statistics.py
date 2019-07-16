import os
import sys

location = ["hongkong", "singapore"]
date = ["19-7-8", "19-7-9", "19-7-10", "19-7-11", "19-7-12"]
website = ["youtube"]


for l in location:
	print(l)

	for w in website:
		cdn_complete_set = {}

		for d in date:
			path = "data/" + l + "/" + d + "/" + w + "/cdns.txt"
			if os.path.exists(path):
				for line in open(path, 'r').readlines():
					domain = line.strip()
					if len(domain):
						cdn_complete_set[domain] = 0
	
		print("total: " + str(len(cdn_complete_set)))
		size_of_complete_set = len(cdn_complete_set)

		# writer = open("data/" + l + "/statistics/" + w + "_cdn_complete_set.txt", "w")
		# for k, v in cdn_complete_set:
		# 	writer.write(url + "\r\n")
		# writer.close()

		# writer = open("data/" + l + "/statistics/" + w + "_cdn_complete_set.txt", "w")
		for d in date:
			path = "data/" + l + "/" + d + "/" + w + "/cdns.txt"
			if os.path.exists(path):
				for line in set(open(path, 'r').readlines()):
					domain = line.strip()
					if len(domain):
						cdn_complete_set[domain] += 1
		
		writer = open("data/" + l + "/statistics/" + w + "_cdn_complete_set.txt", "w")
		for k in cdn_complete_set:
			writer.write("{} {}\r\n".format(k, cdn_complete_set[k]))
		writer.close()

	# writer = open("data/" + l + "/statistics/yt_cdn_proportion.txt", "w")
	# for d in date:
	# 	for w in website:
	# 		path = "data/" + l + "/" + d + "/" + w + "/cdns.txt"
	# 		if os.path.exists(path):
	# 			size = len(set(open(path, 'r').readlines()))
	# 			writer.write(d + " " + str(size / size_of_complete_set) + "\r\n")
	# writer.close()

	# for w in website:
	# 	writer = open("data/" + l + "/statistics/" + w + "_cdn_proportion.txt", "w")
	# 	for d in date:
	# 		path = "data/" + l + "/" + d + "/" + w + "/cdns.txt"
	# 		if os.path.exists(path):
	# 			size = len(set(open(path, 'r').readlines()))
	# 			# writer.write(d + " " + str(size / size_of_complete_set) + "\r\n")
	# 			writer.write("{} {:.3f}\r\n".format(d, size / size_of_complete_set))
	# 	writer.close()

	# print()
