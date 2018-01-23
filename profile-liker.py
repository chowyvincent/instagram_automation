from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


username = sys.argv[1]
password = sys.argv[2]

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

driver.implicitly_wait(10)
x = 0
prev_amt = 0

while x <= 500:
    like_buttons = driver.find_elements_by_css_selector("span[class='_8scx2 coreSpriteHeartOpen']")
    x += len(like_buttons)
    # if prev_amt == x:
    #     print("Hit previous liked images, quitting...")
    #     driver.quit()
    # prev_amt = x
    for y in range(0, len(like_buttons)):
        like_buttons = driver.find_elements_by_css_selector("span[class='_8scx2 coreSpriteHeartOpen']")
        like_buttons[y].click()
        time.sleep(1)
    # for buttons in like_buttons:
    #     buttons.click()
    #     time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print("Scrolled")
    time.sleep(3)
driver.quit()



