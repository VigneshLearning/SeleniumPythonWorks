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

driver.get("https://www.goibibo.com/")
driver.find_element_by_id("gosuggest_inputSrc").click()
driver.find_element_by_id("gosuggest_inputSrc").clear()
driver.find_element_by_id("gosuggest_inputSrc").send_keys("Montevideo (MVD)")
driver.find_element_by_id("gosuggest_inputDest").click()
driver.find_element_by_id("gosuggest_inputDest").clear()
driver.find_element_by_id("gosuggest_inputDest").send_keys("Chennai (MAA)")

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
