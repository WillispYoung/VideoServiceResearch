import sys
import geoip2.database
from ping3 import ping
from find_ips import domain_resolution

# Daily Measurement.

flag = sys.argv[1]

data = open(sys.argv[2], 'r')
output = open(sys.argv[3], 'w')

# input: */cdns.txt
# output: */ips.txt
if flag == '-ip':
	for line in data.readlines():
		domain = line.strip()
		ips = domain_resolution(domain)
		for ip in ips:
			output.write(ip + " ")
		output.write('\n')

# input: */ips.txt
# output: */delays.txt
elif flag == '-ping':
	for line in data.readlines():
		ip = line.strip()
		delay = ping(ip) * 1000 # ms
		output.write(str(delay) + "\n")

# input: */ips.txt
# output: */location.txt
elif flag == "-location":
	reader = geoip2.database.Reader('C:/Python.GeoLite2-City.mmdb')
	for line in data.readlines():
		ip = line.strip()
		res = reader.city(ip)
		try:
			output.write(res.city.name + "\n")
		except Exception:
			output.write('\n')

else:
	sys.exit(0)

data.close()
output.close()
