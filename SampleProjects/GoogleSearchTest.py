from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_Automation(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Montevideo Uruguay")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x.upper())

    def test_search_Kalpesh(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Kalpeshwaran")
        self.driver.find_element_by_name("btnK1").click()
        x = self.driver.title
        print(x.upper())
    @classmethod

    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Mudichachu")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Vignesh/PycharmProjects/Selenium/Reports'))

# if __name__ == '__main__': -- USED to RUN in COMMAND LINE
#     unittest.main()



