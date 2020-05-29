import unittest
import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_xpath("//form[@id='tsf']/div[2]").click()
        time.sleep(4)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "automation step by step - Buscar con Google")

    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Murugesan")
        self.driver.find_element_by_xpath("//form[@id='tsf']/div[2]").click()
        y = self.driver.title
        print(y)
        self.assertEqual(y, "murugesan - Buscar con Google")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()




# if __name__ == '__main__':
#     unittest.main()
