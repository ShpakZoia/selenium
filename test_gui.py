import unittest
from selenium import webdriver

class Checkboxes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        # self.driver.implicitly_wait(10)

    def test_single_checkbox(self):
        checkbox = self.driver.find_element_by_xpath('//input[@id="isAgeSelected"]')
        # checkbox = self.driver.find_element_by_xpath('.//*[@id="isAgeSelected"]').get_attribute("checked")
        checkbox.click()

        show_message_button = self.driver.find_element_by_xpath('//input[@id="isAgeSelected"]')
        assert show_message_button.is_displayed()

    def test_multiple_checkbox(self):
        checkboxes = self.driver.find_elements_by_xpath('//input[@class="cb1-element"]')
        checkbox_list = []
        for check in checkboxes:
            checkbox_list.append(check)

        option_1 = checkbox_list[0].click()
        option_2 = checkbox_list[1].click()
        option_3 = checkbox_list[2].click()
        option_4 = checkbox_list[3].click()

        show_message_button = self.driver.find_element_by_xpath('//input[@id="check1"]')
        assert show_message_button.is_displayed()





    def tearDown(self):
        self.driver.close()