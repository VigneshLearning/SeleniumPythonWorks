from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# Habibi
driver.get("https://youtu.be/BBMH9-fF548?t=101")
time.sleep(7)
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(105)
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(7)
# AbhiyumNaanum
driver.get("https://www.youtube.com/watch?v=sO-3zl44BpA")
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(160)
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(7)
# Theri
driver.get("https://www.youtube.com/watch?v=W-RAUYomJho")
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(190)
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(7)
# YennaiArinthal
driver.get("https://www.youtube.com/watch?v=SdcAN3dobz4")
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(290)
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(7)
# Viswasam
driver.get("https://www.youtube.com/watch?v=-K8Oid03eUU")
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(180)
driver.find_element_by_xpath("//button[@class='ytp-fullscreen-button ytp-button']").click()
time.sleep(12)

driver.close()
driver.quit()
