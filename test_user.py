import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

    def test_user_button(self):
        get_user_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"]')
        get_user_button.click()

        result_loading = self.driver.find_element_by_xpath('//div[@id="loading"]')
        assert result_loading.is_displayed()

    def test_user_img(self):
        get_user_button = self.driver.find_element_by_xpath('//button[@id="save"]')
        get_user_button.click()

        wait_for_img = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "loading")))

        # img = self.driver.find_element_by_xpath('//div[@id="loading"]//img[@src]')
        # assert img.is_displayed()

        img = self.driver.find_element_by_xpath('//div[@id="loading"]')
        assert img.is_displayed()

    def test_last_name(self):
        get_user_button = self.driver.find_element_by_xpath('//button[@id="save"]')
        get_user_button.click()

        last_name = self.driver.find_element_by_xpath('//*[text()[contains(., "Last ")]]')
        assert last_name.is_displayed()








    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
