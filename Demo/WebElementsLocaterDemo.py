from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome("../driver/chromedriver.exe")

driver.get("https://timesheet.ultimatix.net/timesheet/Login/bridge")
driver.maximize_window()

SearchBox = driver.find_element_by_name("form1")
SearchBox.send_keys("597687")
SearchBox = driver.find_element_by_id("proceed-button").click()
time.sleep(35)
SearchBox = driver.find_element_by_id("password-btn").click()
time.sleep(30)
SearchBox = driver.find_element_by_id("password-login").send_keys("Marzo@2020UYU")
SearchBox = driver.find_element_by_id("form-submit").click()
time.sleep(25)
driver.find_element_by_id("menuDropdownImg").click()
driver.find_element_by_class_name("appLinks.ng-binding.ng-scope").click()
time.sleep(40)


#driver.find_element_by_name("btnK").click()

#time.sleep(2)
driver.close()
driver.quit()

print("Podu Thakida Thakida")