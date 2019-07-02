import sys
import dns.resolver

def domain_resolution(domain):
    res = dns.resolver.query(domain)
    res = [str(ip) for ip in res]
    return res


if __name__ == "__main__":
    domain = sys.argv[1]
    print(domain_resolution(domain))

