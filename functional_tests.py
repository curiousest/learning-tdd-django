from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#user visits homepage
		self.browser.get('http://localhost:8000')

		#user looks at page title and heading
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		
#user invited to enter to-do item straight away

#user types "Buy peacock feathers" into text box

#when user hits enter, the page updates, and the page lists "1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"

#The page updates again, and now shows both items on her list

#The user sees that the site has generated a unique URL for their to-do lists
#The user visits the URL and sees that the to-do list is still there

#END

if __name__ == '__main__':
	unittest.main(warnings='ignore')
		


