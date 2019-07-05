import sys
import time
import copy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def scroll_bottom(browser, cycle):
	# scroll to bottom to get more URLs
	script = "var q=document.documentElement.scrollTop={}"
	scroll = 10000
	for i in range(cycle):
		js = script.format(scroll)
		browser.execute_script(js)
		scroll += 500
		time.sleep(0.5)

urls = set()
current_urls = set()
backup_urls = set()

domain = "https://youtube.com"
option = webdriver.ChromeOptions()
option.add_argument("--proxy-server=http://127.0.0.1:8080")

browser = webdriver.Chrome("C:/Python/chromedriver74.exe", options=option)
browser.get(domain)

# find urls on main page
scroll_bottom(browser, 10)
thumbnails = browser.find_elements_by_id("thumbnail")
for element in thumbnails:
	url = element.get_attribute('href')
	if url:
		urls.add(url)
		current_urls.add(url)

time.sleep(1)

print('phase 1 finished.')
print(str(len(urls)) + " urls have been captured.")
print()

# find urls in sub-pages
for i in range(5):
	for url in current_urls:
		browser.get(url)
		browser.execute_script('videos = document.querySelectorAll("video"); for(video of videos) {video.pause()}')
		
		scroll_bottom(browser, 5)
		endpoints = browser.find_elements_by_class_name('yt-simple-endpoint')
		for ep in endpoints:
			url = ep.get_attribute('href')
			if url:
				urls.add(url)
				backup_urls.add(url)

		if len(urls) > 2000:
			browser.close()

			print(str(len(urls)) + " urls have been captured.")
			# print(urls)

			output = open('urls.txt', 'w')
			for url in urls:
				output.write(url + "\n")

			output.close()
			sys.exit(0)

		time.sleep(0.5)

	current_urls = backup_urls
	backup_urls.clear()

	print("phase 2 finished.")
	print(str(len(urls)) + " urls have been captured.")
	print()

browser.close()	

