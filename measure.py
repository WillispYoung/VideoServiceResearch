import sys
import geoip2.database
from ping3 import ping
from find_ips import domain_resolution

# Daily Measurement.

flag = sys.argv[1]

# input: */cdns.txt
# output: */ips.txt
# executed on VM.
if flag == '-ip':
	data = open(sys.argv[2], 'r')
	output = open(sys.argv[3], 'w')
	for line in data.readlines():
		domain = line.strip()
		ips = domain_resolution(domain)
		for ip in ips:
			output.write(ip + " ")
		output.write('\n')

# input: */ips.txt
# output: */delays.txt
# executed on VM.
elif flag == '-ping':
	data = open(sys.argv[2], 'r')
	output = open(sys.argv[3], 'w')
	for line in data.readlines():
		ip = line.strip()
		delay = ping(ip) * 1000 # ms
		output.write(str(delay) + "\n")

# input: */ips.txt
# output: */location.txt
# executed on VM.
elif flag == "-location":
	data = open(sys.argv[2], 'r')
	output = open(sys.argv[3], 'w')
	reader = geoip2.database.Reader('../GeoLite2-City.mmdb')
	# reader2 = geoip2.database.Reader('C:/Python/GeoLite2-Country.mmdb')
	for line in data.readlines():
		ip = line.strip()
		res = reader.city(ip)
		if res.city.name:
			output.write(res.city.name + "\n")
		else:
			output.write(res.country.name + "\n")

# input: location, website
# output: delay information, bad CDN proportion
# executed on VM.
elif flag == "-statistics":
	location = sys.argv[2]
	website = sys.argv[3]
	reader = open("data/{}/statistics/{}_cdn_complete_set.txt".format(location, website), "r")
	

else:
	sys.exit(0)

data.close()
output.close()
