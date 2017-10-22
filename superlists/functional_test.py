import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # confirming website
        self.browser.get('http://localhost:8000')

        # 'To-Do' has written on title and header.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')



        # when you want to add "buy feathers" on the list,

        # you can write it on the textbox.

        # when you push enter key,
        # page is updated and "1: buy feathers" is written on the list.

        # And there is additional textbox to insert additional item.
