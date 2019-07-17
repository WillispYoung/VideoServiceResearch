import sys
import time
import copy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

urls = set()

browser = webdriver.Chrome("C:/Python/chromedriver75.exe")
domain = "https://v.qq.com"

browser.get(domain)

list_items = browser.find_elements_by_class_name("list_item")
for item in list_items:
	url = item.find_element_by_tag_name('a').get_attribute('href')
	urls.add(url)

print(str(len(urls)) + " urls are captured.")

writer = open('tencent_urls.txt', 'w')

for url in urls:
	writer.write(url + "\r\n")

writer.close()

# urls_subset = set()

# count = 0
# for url in urls:
# 	browser.get(url)
# 	list_items = browser.find_elements_by_class_name('list_item')
# 	if len(list_items):
# 		for item in list_items:
# 			try:
# 				url = item.find_element_by_tag_name('a').get_attribute('href')
# 				urls_subset.add(url)
# 			except Exception:
# 				pass
# 	count += 1
# 	if count % 100 == 0:
# 		print("processed " + count + " urls")

# 	time.sleep(1)

# urls = urls.union(urls_subset)

# print(str(len(urls)) + " urls are captured.")

# writer = open('tencent_urls.txt', 'w')

# for url in urls:
# 	writer.write(url + "\r\n")

# writer.close()
