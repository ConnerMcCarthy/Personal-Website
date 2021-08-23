from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
class newVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text for row in rows)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A user wants to create a list and visits the site 
        self.browser.get('http://localhost:8000')
        
        #They notice the header and title mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # They have an option to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Enter a to-do item'
        )

        # They want to pick up some grocieries later and types in "buy wheat bread"
        inputbox.send_keys('buy wheat bread')

        # When they hit enter the page updates, and the page lists "Buy wheat bread" in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        # On the page there is still an option to enter another item. They enter "buy ice cream".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy ice cream')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # The page updates again, and both items are on the list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: buy ice cream')

        # The user wants to save the list, and the site has generated a unique URL to save
        self.fail('Finish the test!')

        # They visit the URL and the list is the same

        # They close the site

    

if __name__ == '__main__':
    unittest.main()



