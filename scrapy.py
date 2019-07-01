import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

domain = "https://youtube.com"
option = webdriver.ChromeOptions()
option.add_argument("--proxy-server=http://127.0.0.1:8080")

browser = webdriver.Chrome("C:/Python/chromedriver74.exe", options=option)
browser.get(domain)

# scroll several times
scrollTop = 10000
script_format = "var q=document.documentElement.scrollTop={}"
for i in range(20):
	js = script_format.format(scrollTop)
	browser.execute_script(js)
	scrollTop += 500
	# print(browser.get_window_size())
	time.sleep(0.5)

# find thumbnails that refer to videos
thumbnails = browser.find_elements_by_id("thumbnail")
for element in thumbnails:
	print(element.get_attribute('href'))

browser.close()
