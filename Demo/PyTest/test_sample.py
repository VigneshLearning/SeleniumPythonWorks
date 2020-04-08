from selenium import webdriver
import time
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Vignesh/PycharmProjects/Selenium/driver/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("Complete")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        x = driver.title
        assert x == "OrangeHRM"
    # @pytest.mark.skip
    @pytest.mark.skip(reason="Not included in this build")
    def test_login_false(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        x = driver.title
        assert x == "OrangeHRm"

    # def test_closure():
    #     driver.close()
    #     driver.quit()
    #     print("Complete")
