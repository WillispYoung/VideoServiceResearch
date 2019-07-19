import sys
import glob
import geoip2.database

from ping3 import ping
from find_ips import domain_resolution

# Daily Measurement.
if len(sys.argv) < 2:
	print("No command is specified!")

else:
	flag = sys.argv[1]

	# Measure all. 
	if flag == '-all':
		location = sys.argv[2]
		website = sys.argv[3]

		files = glob.glob('data/{}/{}/*/cdns.txt'.format(location, website))

		cdn_complete_set = {}
		for file in files:
			for domain in set(open(file, 'r').readline()):
				if domain in cdn_complete_set:
					cdn_complete_set[domain] += 1
				else:
					cdn_complete_set[domain] = 1


