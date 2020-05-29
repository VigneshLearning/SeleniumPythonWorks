import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")



# driver.set_page_load_timeout(10)
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("How to automate test scripts")
driver.find_element_by_xpath("//form[@id='tsf']/div[2]").click()
time.sleep(3)
driver.close()
driver.quit()

print("Podu Thakida Thakida")