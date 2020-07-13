import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class TestSelect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

# Work Select List Demo

    def test_select_one(self):
        select_one = Select(self.driver.find_element_by_id('select-demo'))
        select_one.select_by_value('Sunday')

        select_button = self.driver.find_element_by_xpath('//select[@id="select-demo"] ').click()

        text = self.driver.find_element_by_xpath('//p[@class="selected-value"]')
        assert text.is_displayed()





    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
