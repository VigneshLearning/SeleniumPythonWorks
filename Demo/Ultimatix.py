import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://auth.ultimatix.net/utxLogin/login?TYPE=33554432&REALMOID=06-000e128c-664b-1c1a-9ba7-abcac0a8f081&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-EdbHMX6T+Wb8DN7DVmL5sbY+n+30S7n/gIBptYa9dLbudResX4AYm9ObPeNozoDH&TARGET=-SM-HTTPS%3A%2F%2Fwww.ultimatix.net%2FutxHomeApp%2FredirectToHome%3FTARGET%3Dhttps-%3A-%2F-%2Fwww.ultimatix.net-%2Fcontent-%2FultimatixPortal-%2Fultimatixportalhome.html")
driver.find_element_by_xpath("//input[@id='form1']").send_keys('597687')
driver.find_element_by_xpath("//button[@id='proceed-button']").click()
time.sleep(3)
driver.find_element_by_xpath("//button[@id='password-btn']").click()
time.sleep(120)
driver.find_element_by_xpath("//input[@id='password-login']").send_keys("Abril@2020UYU")
driver.find_element_by_xpath("//button[@id='form-submit']").click()
time.sleep(15)
# TIMESHEET PAGES
# driver.find_element_by_xpath("//a[@class='listviewtext ng-binding ng-scope'][contains(text(),'Timesheet Entry')]").click()
# time.sleep(15)
# driver.find_element_by_xpath("//div[@id='ultimatixAlertPopUp']//input[@class='button buttonClass']").click()
# time.sleep(10)
driver.find_element_by_xpath("//a[@class='listviewtext ng-binding ng-scope'][contains(text(),'Health Insurance Portal')]").click()
time.sleep(20)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
x = driver.title
print(x)
window_before = driver.window_handles[0]
driver.switch_to.window(window_before)
time.sleep(2)
x = driver.title
print(x)
driver.find_element_by_xpath("//a[@class='listviewtext ng-binding ng-scope'][contains(text(),'Timesheet Entry')]").click()
time.sleep(15)
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
x = driver.title
print(x)
time.sleep(3)
# driver.find_element_by_name("q").send_keys("Automation Step by Step")
# time.sleep(2)
# driver.find_element_by_name("btnK").click()
# print(driver.title)

# USE IT WHEN U NEED IT

# driver.close()
# driver.quit()

print("Completed")
