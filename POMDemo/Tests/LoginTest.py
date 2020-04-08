from selenium import webdriver
import time
import unittest
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_name("Submit").click()
        # time.sleep(5)
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(5)

    @classmethod

    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Success")
