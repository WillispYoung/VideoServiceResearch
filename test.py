from ping3 import ping

from find_traces import track
from find_ips import domain_resolution


data = open('data/yt_cdn.txt', 'r')
res = open('data/yt_delay_singapore.txt', 'w')

count = 0
delays = []
for line in data.readlines():
    if count > 2:
        domain = line.strip()
        delay = ping(domain) * 1000 # ms
        res.write(str(delay) + "\n")
        delays.append(delay)
#        ips = domain_resolution(domain)
#        print(ips)
#        for ip in ips:
#            res.write(ip + " ")
#        res.write("\n")
#        if len(ips) > 1:
#            extra.append(domain)
    count += 1

#print(extra)

data.close()
res.close()
