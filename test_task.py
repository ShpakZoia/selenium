import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class TestTable(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='d:\зоя\Chrome\chromedriver')
        self.url = self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")

    def test_all_rows(self):
        wait_for_rows = WebDriverWait(self.driver, 5)
        all_rows = self.driver.find_elements_by_xpath('//table[@id="task-table"]//tbody//tr')
        assert len(all_rows) == 7

    def test_all_rows_incorrect(self):
        all_rows = self.driver.find_elements_by_xpath('//table[@id="task-table"]//tbody//tr')
        assert len(all_rows) == 6

    def test_task_filter(self):
        enter_task = self.driver.find_element_by_xpath('//input[@id="task-table-filter"]')
        enter_task.send_keys('Wireframes')

        row = self.driver.find_element_by_xpath('//table[@id="task-table"]//td[contains(text(),"Wireframes")]')
        assert row.is_displayed()

    def test_letter_filter(self):
        enter_letter = self.driver.find_element_by_id('task-table-filter')
        enter_letter.send_keys('b')

        all_results = self.driver.find_elements_by_xpath('//table[@id="task-table"]/tbody/tr[not(contains(@style,"display: none;"))]')
        assert len(all_results) == 5

    def test_result(self):
        all_results = self.driver.find_elements_by_xpath('//table[@id="task-table"]//td[contains(text(),"Bootstrap")]')
        results = []
        for i in all_results:
            results.append(i.text)
        assert 'Bootstrap 3' in results




    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
