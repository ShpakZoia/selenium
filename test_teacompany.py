import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestTea_company(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("http://www.practiceselenium.com/check-out.html")

    def test_billing_information(self):
        e_mail = self.driver.find_element_by_xpath('//input[@id="email"]')
        e_mail.clear()
        e_mail.send_keys('email@gmail.com')

        name = self.driver.find_element_by_xpath('//input[@id="name"]')
        name.clear()
        name.send_keys('name')

        address = self.driver.find_element_by_xpath('//textarea[@id="address"]')
        address.clear()
        address.send_keys('name')

        card_type = Select(self.driver.find_element_by_id('card_type'))
        card_type.select_by_visible_text('Visa')

        card_number = self.driver.find_element_by_xpath('//input[@id="card_number"]')
        card_number.clear()
        card_number.send_keys('12345')

        cardholder_name = self.driver.find_element_by_xpath('//input[@id="cardholder_name"]')
        cardholder_name.clear()
        cardholder_name.send_keys('name')

        verification_code = self.driver.find_element_by_xpath('//input[@id="card_number"]')
        verification_code.clear()
        verification_code.send_keys('12345')

        button = self.driver.find_element_by_xpath('//button[contains(text(), "Place Order")]')
        button.click()

















    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
