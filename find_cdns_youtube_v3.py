import re
import sys
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Find 10,000+ pages.
def find_webpages():
	# Output: URL set
	urls = set()

	domain = "https://youtube.com"
	option = webdriver.ChromeOptions()
	option.add_argument("--proxy-server=http://127.0.0.1:8080")

	browser = webdriver.Chrome("C:/Python/chromedriver75.exe", options=option)
	browser.get(domain)

	# Javascript: scroll page down to get more elements.
	# var h = Math.max(
	#     document.documentElement["clientHeight"],
	#     document.body["scrollHeight"],
	#     document.documentElement["scrollHeight"],
	#     document.body["offsetHeight"],
	#     document.documentElement["offsetHeight"]
	# );
	# window.scrollTo(0,h+1000);

	cmd = 'var h = Math.max(document.documentElement["clientHeight"],document.body["scrollHeight"],document.documentElement["scrollHeight"],document.body["offsetHeight"],document.documentElement["offsetHeight"]);window.scrollTo(0,h+1000);'

	# scroll 20 times
	for i in range(1, 20):
		browser.execute_script(cmd)
		time.sleep(1)
	
	endpoints = browser.find_elements_by_class_name("yt-simple-endpoint")
	for ep in endpoints:
		url = ep.get_attribute('href')
		if url:
			# Format: https://www.youtube.com/watch?v=* (no other parameters)
			url = url.split('&')[0]
			urls.add(url)
		
	if len(urls) > 10000:
		return urls

	print("{} pages have been captured".format(len(urls)))

	links_per_page = int(10000 / len(urls))

	page_entrances = urls.copy()
	for page in page_entrances:
		browser.get(page)
		endpoints = browser.find_elements_by_class_name('yt-simple-endpoint')

		count = 0
		while len(endpoints) < links_per_page and count < 4:
			browser.execute_script(cmd)
			time.sleep(0.5)
			count += 1
			endpoints = browser.find_elements_by_class_name('yt-simple-endpoint')

		for ep in endpoints:
			url = ep.get_attribute('href')
			if url:
				url = url.split('&')[0]
				urls.add(url)

	print("{} pages have been captured".format(len(urls)))

	return urls


# Find 300+ CDNs.
def find_cdns(url_file, cdn_file):
	proxies = {
		"http": "http://127.0.0.1:8080",
		"https": "https://127.0.0.1:8080"
	}

	urls = open(url_file, "r").readlines()
	output = open(cdn_file, "w")

	pattern = r"r\d-{3}\w{2}-\S{8}.googlevideo.com"

	count = 1
	for url in urls:
		# response = requests.get(url, proxies=proxies).content.decode("utf-8")
		response = requests.get(url).content.decode("utf-8")
		cdns = set(re.findall(pattern, response))
		if len(cdns) > 0:
			for cdn in cdns:
				output.write(cdn + " ")
			output.write("\n")

		if count % 100 == 0:
			print("{} URLs processed".format(count))
		count += 1

	return


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("No argument specified")
		sys.exit(0)
	
	flag = sys.argv[1]

	if flag == "0":
		output_file = open(sys.argv[2], 'w')
		urls = find_webpages()
		for url in urls:
			output_file.write(url + "\n")
		output_file.close()
		print("Capture finished.")

	elif flag == "1":
		find_cdns(sys.argv[2], sys.argv[3])
		print("Measurement finished.")

	else:
		print("Wrong argument")
		sys.exit(0)

