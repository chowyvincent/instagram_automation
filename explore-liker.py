from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import sys


username = sys.argv[1]
password = sys.argv[2]
inputHashTag = sys.argv[3]
indexVal = int(sys.argv[4])
maxCounter = 0

def runScript(startIndex):

	x = startIndex
	prev_amt = 0
	global maxCounter
	while True and maxCounter < 400:
		total_pictures = driver.find_elements_by_css_selector("div[class='_si7dy']")
		if prev_amt == len(total_pictures):
			print("Length did not update, prev_amt:", prev_amt)
			print("Rerun with x:" + str(len(total_pictures) + 1))
			driver.get("https://www.instagram.com/explore/tags/" + inputHashTag + "/")
			runScript(len(total_pictures) + 1)
		prev_amt = len(total_pictures)
		while x < len(total_pictures) and maxCounter < 400:
			print("current:", x)
			pictures = driver.find_elements_by_css_selector("div[class='_si7dy']")
			picture = pictures[x]
			time.sleep(.5)
			picture.click()
			time.sleep(.5)
			# picture.click()
			# time.sleep(1)

			print("Inside")
			time.sleep(.5)
			like_buttons = driver.find_elements_by_css_selector("span[class='_8scx2 coreSpriteHeartOpen']")

			if len(like_buttons) > 0:
				like_buttons[0].click()
				print("liked")
				maxCounter += 1

			time.sleep(.5)
			escape_button = driver.find_elements_by_css_selector("button[class='_dcj9f']")
			if(len(escape_button) == 0):
				print("Caught error page")
				x += 1
				print("Rerun with x:", x)
				driver.get("https://www.instagram.com/explore/tags/" + inputHashTag + "/")
				runScript(x)			
			else:
				escape_button[0].click()

			time.sleep(.5)
			x += 1

		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
		time.sleep(1)

# Execution starts here, the setup
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME,"_b93kq"))
	)
finally:
	element.click()

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.NAME,"username"))
	)
finally:
	element.send_keys(username)

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.NAME,"password"))
	)
finally:
	element.send_keys(password)

element = driver.find_element_by_tag_name('button')
element.click()

# driver.implicitly_wait(20)

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='_avvq0 _o716c']"))
	)
finally:
	element.send_keys("#" + inputHashTag)
	element.send_keys(u'\ue007')
	time.sleep(1)

hashtags = driver.find_elements_by_class_name("_t3f9x")
hashtags[0].click()
time.sleep(1)

# # Pictures listed from here
# try:
# 	element = WebDriverWait(driver, 10).until(
# 		EC.presence_of_element_located((By.CLASS_NAME, "_myci9"))
# 	)
# finally:
# 	time.sleep(2)

# try:
# 	element = WebDriverWait(driver, 10).until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='_8mlbc _vbtk2 _t5r8b']"))
# 	)
# finally:
# 	print("Running Script")
runScript(indexVal)
driver.quit()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# #Load more
# load_more = driver.find_elements_by_css_selector("a[class='_8imhp _glz1g']")
# load_more[0].click()
# print("clicked load more")
# time.sleep(1)
