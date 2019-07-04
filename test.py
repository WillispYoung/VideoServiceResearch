from ping3 import ping

from find_traces import track
from find_ips import domain_resolution


data1 = open('data/yt_cdn.txt', 'r')
data2 = open('data/yt_delay_hongkong.txt', 'r')
# res = open('data/yt_delay_hongkong.txt', 'w')


count = 0
cdns = []
delays = []
for line in data1.readlines():
    if count > 2:
        domain = line.strip()
        cdns.append(domain)
        # delay = ping(domain) * 1000 # ms
        # res.write(str(delay) + "\n")
        # delays.append(delay)
#        ips = domain_resolution(domain)
#        print(ips)
#        for ip in ips:
#            res.write(ip + " ")
#        res.write("\n")
#        if len(ips) > 1:
#            extra.append(domain)
    count += 1

for line in data2.readlines():
	delay = float(line.strip())
	delays.append(delay)

assert len(cdns) == len(delays)

good_cdns = []
bad_cdns = []

for i in range(len(cdns)):
	if delays[i] > 50:
		bad_cdns.append((cdns[i], delays[i]))
	else:
		good_cdns.append((cdns[i], delays[i]))

output = open('data/yt_good_bad_cdns.txt', 'w')
output.write("Good CDNs\n")

for cdn in good_cdns:
	output.write(cdn[0] + " " + str(cdn[1]) + "\n")

output.write("Bad CDNs\n")
for cdn in bad_cdns:
	output.write(cdn[0] + " " + str(cdn[1]) + "\n")

#print(extra)

data1.close()
data2.close()
output.close()
# res.close()
