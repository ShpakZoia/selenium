import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class TestDropdown_Days_in_week(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        self.assertIn('Selenium', self.driver.title)

    def test_sunday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Sunday')
        assert 'Day selected :- Sunday' in self.driver.page_source

    def test_monday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Monday')
        assert 'Day selected :- Monday' in self.driver.page_source

    def test_tuesday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Tuesday')
        assert 'Day selected :- Tuesday' in self.driver.page_source

    def test_wednesday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Wednesday')
        assert 'Day selected :- Wednesday' in self.driver.page_source

    def test_thursday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Thursday')
        assert 'Day selected :- Thursday' in self.driver.page_source

    def test_friday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Friday')
        assert 'Day selected :- Friday' in self.driver.page_source

    def test_saturday(self):
        button = Select(self.driver.find_element_by_id('select-demo'))
        button.select_by_visible_text('Saturday')
        assert 'Day selected :- Saturday' in self.driver.page_source

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
