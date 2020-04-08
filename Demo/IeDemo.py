import time

from selenium import webdriver

path = "../driver/IEDriverServer.exe"

driver = webdriver.Ie(executable_path=path)

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("How to automate test scripts")
driver.find_element_by_name("btnK").click()
time.sleep(5)

driver.quit()

print("Podu Thakida Thakida")
