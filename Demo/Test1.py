import time

from selenium import webdriver

driver = webdriver.Chrome("../driver/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("How to automate test scripts")

time.sleep(3)

driver.find_element_by_name("btnK").click()

time.sleep(3)

driver.close()
driver.quit()

print("Podu Thakida Thakida")