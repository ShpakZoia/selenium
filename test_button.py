import unittest
from selenium import webdriver


class RadioButton(unittest.TestCase):
   def setUp(self):
       self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
       self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

   def test_button_male(self):
       button_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="optradio"]')
       button_male.click()

       check_button = self.driver.find_element_by_id('buttoncheck')
       check_button.click()

       get_checked_value = self.driver.find_element_by_xpath('//p[contains(text(), "Male")]')
       assert get_checked_value.is_displayed()

   def test_button_female(self):
       button_female = self.driver.find_element_by_xpath('//input[@value="Female"][@name="optradio"]')
       button_female.click()

       check_button = self.driver.find_element_by_id('buttoncheck')
       check_button.click()

       get_checked_value = self.driver.find_element_by_xpath('//p[contains(text(), "Female")]')
       assert get_checked_value.is_displayed()

   def test_group_button(self):
       button_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
       button_male.click()

       button_male_age_1 = self.driver.find_element_by_xpath('//input[@value="0 - 5"]')
       button_male_age_1.click()

       button_male_age_2 = self.driver.find_element_by_xpath('//input[@value="5 - 15"]')
       button_male_age_2.click()

       button_male_age_3 = self.driver.find_element_by_xpath('//input[@value="15 - 50"]')
       button_male_age_3.click()

       button_get_values = self.driver.find_element_by_xpath('//button[@onclick="getValues();"]')
       button_get_values.click()

       show_message_button = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
       assert show_message_button.is_displayed()

       button_female = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
       button_female.click()

       button_female_age_1 = self.driver.find_element_by_xpath('//input[@value="0 - 5"]')
       button_female_age_1.click()

       button_female_age_2 = self.driver.find_element_by_xpath('//input[@value="5 - 15"]')
       button_female_age_2.click()

       button_female_age_3 = self.driver.find_element_by_xpath('//input[@value="15 - 50"]')
       button_female_age_3.click()

       button_get_values = self.driver.find_element_by_xpath('//button[@onclick="getValues();"]')
       button_get_values.click()

       show_message_button = self.driver.find_element_by_xpath('')
       assert show_message_button.is_displayed()

   def tearDown(self):
       self.driver.close()


if __name__ == '__main__':
    unittest.main()
