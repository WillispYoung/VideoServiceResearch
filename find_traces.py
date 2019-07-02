import re
import sys
import subprocess


def track(domain):
    cmd = subprocess.Popen(['traceroute','-n', domain], stdout=subprocess.PIPE)
    output = cmd.stdout
    line = output.readline()
    count = 0
    res = []
    # pattern = re.compile('\d+\.\d+')
    while line:
        if count > 0:
            words = line.split()
            words = [i.decode('utf-8') for i in words]
            # print(words)
            line_res = []
            i = 1
            while i < len(words):
                if words[i] == '*':
                    i += 1
                elif not bool(re.match('\d+\.\d+\.\d+\.\d+', words[i])):
                    i += 2
                else:
                    line_res.append(words[i])
                    i += 3
            res.append(line_res)
        count += 1
        line = output.readline()
    print(res)
    return res


if __name__ == "__main__":
    domain = sys.argv[1]
    track(domain)

