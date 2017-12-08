import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # when you heard about new application for working list,
        # you would confirm that website.
        self.browser.get('http://localhost:8000')

        # 'To-Do' has written on title and header.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # work is added
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'inserting working item'
        )

        # when you want to add "buy feathers" on the list,
        # you can write it on the textbox.
        inputbox.send_keys('buying feather')

        # when you push enter key,
        # page is updated and "1: buy feathers" is written on the list.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: buying feather' for row in rows),
        )

        # And there is additional textbox to insert additional item.
        # add 'make fishnet using feather'.
        self.fail('Finish the test!')

        # page is updated and two item appears on the list.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
