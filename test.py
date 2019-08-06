# import re
# import requests

# url = "https://www.youtube.com/watch?v=z0grXGgO9DY"

# proxies = {
#     "http": "http://127.0.0.1:8080",
#     "https": "https://127.0.0.1:8080"
# }

# response = requests.get(url, proxies=proxies).content.decode("utf-8").split("\n")

# pattern = r"r\d-{3}\w{2}-\S{8}.googlevideo.com"

# for line in response:
#     res = re.findall(pattern, line)
#     if len(res) > 0:
#         print(res)

# line = " https://r5---sn-i3b7knld.googlevideo.com/generate_20"

# print(re.findall(pattern, line))

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

# urls = open("data/urls/youtube-v1.txt", "r").readlines()

# option = webdriver.ChromeOptions()
# option.add_argument("--proxy-server=http://127.0.0.1:8080")
# browser = webdriver.Chrome("C:/Python/chromedriver75.exe", options=option)

# for url in urls:
#         browser.get(url)
#         time.sleep(0.3)

# cmd = 'var h = Math.max(document.documentElement["clientHeight"],document.body["scrollHeight"],document.documentElement["scrollHeight"],document.body["offsetHeight"],document.documentElement["offsetHeight"]);window.scrollTo(0,h+1000);'

# browser.execute_script(cmd)

# import re

# lines = open("urls.txt", "r").readlines()
# res = set()

# # print(lines[0])

# for line in lines:
#     line = line.strip()
#     # print(line)
#     if "https://www.youtube.com/watch?v" in line:
#         res.add(line)

# print(len(res))

# writer = open("urls.txt", "w")
# for line in res:
#     writer.write(line + "\n")
# writer.close()


# import matplotlib.pyplot as plt

# figure = plt.figure()
# axis = figure.add_subplot(1, 1, 1)

# axis.scatter([2, 3, 4])

# plt.show()

# print(bin(185)[2:])
# print(bin(167)[2:])
# print(bin(7)[2:])

# print("a", end='')
# print("b")