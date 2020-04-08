from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProjects.Pages.loginPages import LoginPages
from SampleProjects.Pages.homePages import HomePages
import HtmlTestRunner

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPages(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePages(driver)
        time.sleep(5)
        homepage.click_welcome()
        time.sleep(5)
        homepage.click_logout()
        time.sleep(5)

        # driver.find_element_by_name("txtUsername").send_keys("Admin")
        # driver.find_element_by_name("txtPassword").send_keys("admin123")
        # driver.find_element_by_name("Submit").click()
        # time.sleep(5)
        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()
        # time.sleep(4)
        print("YoU CaN Do iT")

    @classmethod

    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Vignesh/PycharmProjects/Selenium/Reports'),verbosity=2)


# driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_name("txtPassword").send_keys("admin123")
# driver.find_element_by_name("Submit").click()
# time.sleep(5)
# driver.find_element_by_id("welcome").click()
# driver.find_element_by_link_text("Logout").click()
# time.sleep(4)
# print("YoU CaN Do iT")
# driver.close()
# driver.quit()