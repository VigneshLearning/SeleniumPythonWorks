import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options


# chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.santander.com.uy/")
driver.find_element_by_id("ingresar").click()
driver.find_element_by_id("paisS").click()
s1 = Select(driver.find_element_by_id('paisS'))
s1.select_by_visible_text('Otro')
driver.find_element_by_id("otros").click()
s1 = Select(driver.find_element_by_id('otros'))
time.sleep(5)
s1.select_by_visible_text('India')
time.sleep(7)
driver.find_element_by_xpath("//input[@id='documento_persona']").send_keys("K2499214")
driver.find_element_by_xpath("//form[@id='formLogin']//button[@class='btn btn--main-color btn-block'][contains(text(),'Ingresar')]").click()
time.sleep(20)
driver.find_element_by_xpath("//input[@id='ctl00_MainHolder_LoginControlPeople_textPasswordVisible']").click()
driver.find_element_by_xpath("//input[@id='ctl00_MainHolder_LoginControlPeople_textPasswordVisible']").send_keys("fuckyou")

driver.find_element_by_xpath("//a[@id='ctl00_MainHolder_LoginControlPeople_lnkLogin']").click()
time.sleep(40)

driver.close()
driver.quit()

print("Completed")
