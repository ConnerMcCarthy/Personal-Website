from selenium import webdriver
import unittest
class newVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A user wants to create a list and visits the site 
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!') 

        # They have an option to enter a to-do item

        # They want to pick up some grocieries later and types in "buy wheat bread"

        # When they hit enter the page updates, and the page lists "Buy wheat bread" in the to-do list

        # On the page there is still an option to enter another item. They enter "buy ice cream".

        # The page updates again, and both items are on the list

        # The user wants to save the list, and the site has generated a unique URL to save

        # They visit the URL and the list is the same

        # They close the site

    

if __name__ == '__main__':
    unittest.main()



