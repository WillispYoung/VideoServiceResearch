import os
import sys 
# import glob
import geoip2.database

from ping3 import ping
from find_ips import domain_resolution

# CDN statistics.

if len(sys.argv) < 2:
	print("No command is specified!")

else:
	location = sys.argv[1]
	website = sys.argv[2]
	date = sys.argv[3]

	if website == "youtube":
		cdn_file = open('data/{}/{}/{}/cdns.txt'.format(location, website, date), "r").read().split()
		frequency = {}

		for cdn in cdn_file:
			if cdn in frequency:
				frequency[cdn] += 1
			else:
				frequency[cdn] = 1
		
		output = open('data/{}/{}/{}/stats.txt'.format(location, website, date), "w")
		lib = geoip2.database.Reader("../GeoLite2-City.mmdb")
		for cdn in frequency:
			output.write(cdn + " " + str(frequency[cdn]) + " ")

			ips = domain_resolution(cdn)
			if len(ips) == 0:
				output.write("\n")
				continue
			else:
				output.write(ips[0] + " ")
			
			delay = "{:.3f}".format(ping(ips[0]) * 1000)
			output.write(delay + " ")

			res = lib.city(ips[0])
			if res.city.name:
				output.write(res.city.name + " ")
			elif res.country.name:
				output.write(res.country.name + " ")
			else:
				output.write("unk ")

			output.write("\n")
		
		output.close()


	# if flag == '-default':
	# 	location = sys.argv[2]
	# 	website = sys.argv[3]
	# 	week = sys.argv[4]

	# 	files = glob.glob('data/{}/{}/measure/{}/cdns*.txt'.format(location, website, week))

	# 	cdn_complete_set = {}
	# 	for file in files:
	# 		for line in open(file, 'r').readlines():
	# 			items = line.split(' ')
	# 			if items[0] in cdn_complete_set:
	# 				cdn_complete_set[items[0]] += int(items[1])
	# 			else:
	# 				cdn_complete_set[items[0]] = int(items[1])

	# 	path = 'data/{}/{}/statistics/{}/'.format(location, website, week)
		
	# 	if not os.path.exists(path):
	# 		os.mkdir(path)

	# 	writer = open(path + 'cdn_stats.txt', 'w')
		
	# 	for domain in cdn_complete_set:
	# 		writer.write(domain + "|")
	# 		writer.write(str(cdn_complete_set[domain]) + "|")

	# 		ips = domain_resolution(domain)

	# 		for i in range(len(ips) - 1):
	# 			writer.write(ips[i] + ",")
	# 		writer.write(ips[-1] + "|")

	# 		delays = []
	# 		for ip in ips:
	# 			delay = "{:.3f}".format(ping(ip) * 1000)
	# 			delays.append(delay)

	# 		for i in range(len(delays) - 1):
	# 			writer.write(delays[i] + ",")
	# 		writer.write(delays[-1] + "|")

	# 		# locations = []
	# 		# reader = geoip2.database.Reader("../GeoLite2-City.mmdb")
	# 		# for ip in ips:
	# 		# 	result = reader.city(ip)
	# 		# 	if result.city.name:
	# 		# 		locations.append(result.city.name)
	# 		# 	elif result.country.name:
	# 		# 		locations.append(result.country.name)
	# 		# 	else:
	# 		# 		locations.append("unknown")

	# 		# for i in range(len(locations) - 1):
	# 		# 	writer.write(locations[i] + ",")
	# 		# writer.write(locations[-1] + "\n")

	# 	writer.close()
