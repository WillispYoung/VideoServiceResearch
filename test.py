import sys
from find_ips import domain_resolution

data = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

for line in data.readlines():
	domain = line.strip()
	ips = domain_resolution(domain)
	for ip in ips:
		output.write(ip + " ")
	output.write('\n')

data.close()
output.close()
