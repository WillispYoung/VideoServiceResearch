from find_traces import track
from find_ips import domain_resolution

data = open('data/yt_cdn.txt', 'r')
res = open('data/yt_ip_hongkong.txt', 'w')

count = 0
extra = []
for line in data.readlines():
    if count > 2:
        domain = line.strip()
        ips = domain_resolution(domain)
#        print(ips)
        for ip in ips:
            res.write(ip + " ")
        res.write("\n")
        if len(ips) > 1:
            extra.append(domain)
    count += 1

print(extra)

data.close()
res.close()
