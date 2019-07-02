import matplotlib.pyplot as plt

data1 = [float(line) for line in open("data/yt_delay_singapore.txt", 'r').readlines()]
data2 = [float(line) for line in open("data/yt_delay_hongkong.txt", 'r').readlines()]

proportion = [data1[i] / data2[i] for i in range(len(data1))]

# data.sort()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set_title("Delay in Hong Kong")
# ax.plot(proportion)
ax.plot(data2)

# plt.ylabel("delay | ms")
plt.show()
