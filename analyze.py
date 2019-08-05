import sys
import glob
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("No argument specified")
    sys.exit(0)

flag = sys.argv[1]

if flag == "-diff":
    location = sys.argv[2]
    website = sys.argv[3]

    data_files = glob.glob("data/{}/{}/*/stats.txt".format(location, website))
    data_files = [f.replace("\\", "/") for f in data_files]

    # print(data_files)

    dates = [f.split("/")[3] for f in data_files]
    data = []

    for f in data_files:
        lines = open(f, "r").readlines()
        record = {}
        for line in lines:
            items = line.split()
            record[items[0]] = items[1:]
        data.append(record)

    for i in range(len(data_files)):
        for j in range(i + 1, len(data_files)):
            difference = 0
            domains1 = set(data[i].keys())
            domains2 = set(data[j].keys())
            shared_domains = domains1.intersection(domains2)

            for domain in shared_domains:
                if data[i][domain][1] != data[j][domain][1]:
                    difference += 1
            
            print("{} {} ({} domains) : {}".format(dates[i], dates[j], len(shared_domains), difference))

elif flag == "-freq":
    location = sys.argv[2]
    website = sys.argv[3]

    data_files = glob.glob("data/{}/{}/*/stats.txt".format(location, website))
    data_files = [f.replace("\\", "/") for f in data_files]

    # print(data_files)

    dates = [f.split("/")[3] for f in data_files]
    data = []

    for f in data_files:
        lines = open(f, "r").readlines()
        record = {}
        for line in lines:
            items = line.split()
            record[items[0]] = items[1:]
        data.append(record)

    all_domains = set()
    for record in data:
        all_domains = all_domains.union(set(record.keys()))
    
    all_domains = list(all_domains)
    print("{} domains captured".format(len(all_domains)))

    freqs = []
    # for record in data:
    #     x = []
    #     y = []
    #     for i in range(len(all_domains)):
    #         if all_domains[i] in record:
    #             x.append(i)
    #             y.append(int(record[all_domains[i]][0]))
    #     freqs.append((x,y))

    for i in range(len(all_domains)):
        x = []
        y = []
        for record in data:
            if all_domains[i] in record:
                x.append(i)
                y.append(int(record[all_domains[i]][0]))
        freqs.append((x,y))
    
    figure = plt.figure()
    axis = figure.add_subplot(1, 1, 1)
    axis.set_title("Frequency in {}".format(location.title()))

    # for i in range(len(freqs)):
    #     axis.scatter(freqs[i][0], freqs[i][1], s=3, label=dates[i])

    for line in freqs:
        if max(line[1]) - min(line[1]) < 10:  # how to set this threshold?
            avg = int(sum(line[1]) / len(line[1]))
            axis.plot(line[0][0], avg, marker='o', markersize=2)
        else:
            axis.plot(line[0], line[1], marker='o', markersize=3)
    
    plt.xlabel("Domain ID")
    plt.ylabel("Frequency")
    # plt.yscale("log")
    # plt.legend()
    plt.show()

elif flag == "-delay":
    location = sys.argv[2]
    website = sys.argv[3]

    data_files = glob.glob("data/{}/{}/*/stats.txt".format(location, website))
    data_files = [f.replace("\\", "/") for f in data_files]

    # print(data_files)

    dates = [f.split("/")[3] for f in data_files]
    data = []

    for f in data_files:
        lines = open(f, "r").readlines()
        record = {}
        for line in lines:
            items = line.split()
            record[items[0]] = items[1:]
        data.append(record)

    all_domains = set()
    for record in data:
        all_domains = all_domains.union(set(record.keys()))
    
    all_domains = list(all_domains)
    print("{} domains captured".format(len(all_domains)))

    delays = []
    # for record in data:
    #     x = []
    #     y = []
    #     for i in range(len(all_domains)):
    #         if all_domains[i] in record:
    #             if record[all_domains[i]][2] != "unk":
    #                 x.append(i)
    #                 y.append(int(float(record[all_domains[i]][2])))
    #     freqs.append((x,y))

    for i in range(len(all_domains)):
        x = []
        y = []
        for record in data:
            if all_domains[i] in record:
                if record[all_domains[i]][2] != 'unk':
                    x.append(i)
                    y.append(int(float(record[all_domains[i]][2])))
        if len(x) > 0:
            delays.append((x, y))
    
    figure = plt.figure()
    axis = figure.add_subplot(1, 1, 1)
    axis.set_title("Delay in {}".format(location.title()))

    # for i in range(len(freqs)):
    #     axis.scatter(freqs[i][0], freqs[i][1], s=3, label=dates[i])
    
    for delay in delays:
        try:
            if max(delay[1]) - min(delay[1]) < 30:  # how to set this threshold?
                avg = int(sum(delay[1]) / len(delay[1]))
                axis.plot(delay[0][0], avg, marker='o', markersize=2)
            else:
                axis.plot(delay[0], delay[1], marker='o', markersize=3)
        except Exception:
            print("error plot {}".format(delay))

    plt.xlabel("Domain ID")
    plt.ylabel("Ping Delay (ms)")
    # plt.legend()
    plt.show()

elif flag == "-quality":
    location = sys.argv[2]
    website = sys.argv[3]

    data_files = glob.glob("data/{}/{}/*/stats.txt".format(location, website))
    data_files = [f.replace("\\", "/") for f in data_files]

    # print(data_files)

    dates = [f.split("/")[3] for f in data_files]
    data = []

    for f in data_files:
        lines = open(f, "r").readlines()
        record = {}
        for line in lines:
            items = line.split()
            record[items[0]] = items[1:]
        data.append(record)
    
    for i in range(len(dates)):
        count = 0
        freq_count = 0
        freq_sum = 0
        for key in data[i]:
            if data[i][key][2] != 'unk':
                # print(data[i][key][2])
                if int(float(data[i][key][2])) > 100:
                    count += 1
                    freq_count += int(data[i][key][0])
            freq_sum += int(data[i][key][0])
        print("{} : {:.2f}, {:.2f}".format(dates[i], count/len(data[i]), freq_count/freq_sum))

elif flag == "-subnet":
    location = sys.argv[2]
    website = sys.argv[3]

    data_files = glob.glob("data/{}/{}/*/stats.txt".format(location, website))
    data_files = [f.replace("\\", "/") for f in data_files]

    # print(data_files)

    dates = [f.split("/")[3] for f in data_files]
    data = []

    for f in data_files:
        lines = open(f, "r").readlines()
        record = set()
        for line in lines:
            items = line.split()
            ip = items[2].split(".")
            subnet = ip[0] + "." + ip[1]
            record.add(subnet)
        record = list(record)
        data.append(record)
    
    for i in range(len(data)):
        print("- | " + dates[i] + " | ", end='')
        data[i].sort()
        for subnet in data[i]:
            print(subnet + ", ", end='')
        print()

elif flag == "-geo":

    