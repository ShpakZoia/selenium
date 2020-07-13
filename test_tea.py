import unittest
from selenium import webdriver


class TestTalk_tea(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("http://www.practiceselenium.com/let-s-talk-tea.html")

    def test_information(self):
        name = self.driver.find_element_by_xpath('//input[@name="name"]')
        name.clear()
        name.send_keys('name')

        e_mail = self.driver.find_element_by_xpath('//input[@name="email"]')
        e_mail.clear()
        e_mail.send_keys('email@gmail.com')


        subject = self.driver.find_element_by_xpath('//input[@name="subject"]')
        subject.clear()
        subject.send_keys('name')

        message = self.driver.find_element_by_xpath('//textarea[@name="message"]')
        message.clear()
        message.send_keys('hello')

        submit = self.driver.find_element_by_xpath('//input[@value="Submit"]')
        submit.click()







    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
