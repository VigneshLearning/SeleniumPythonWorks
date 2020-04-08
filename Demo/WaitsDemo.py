from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
# driver.implicitly_wait(4)
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Murugesan Selvi")
wait = WebDriverWait(driver, 10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("Element is clickable")
except:
    print("Element is not Clickable")
    exit(1)
element.click()
# driver.find_element_by_name("btnK").click()

print("Podra Vediya")
driver.close()
driver.quit()
