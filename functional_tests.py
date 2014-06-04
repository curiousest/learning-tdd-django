from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		
		#user invited to enter to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		#user types "Buy peacock feathers" into text box
		inputbox.send_keys('Buy peacock feathers')

		#when user hits enter, the page updates, and the page lists "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		
		#There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to be stupid')
		inputbox.send_keys(Keys.ENTER)

		#The page updates again, and now shows both items on her list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn('2: Use peacock feathers to be stupid', [row.text for row in rows])
		
		#The user sees that the site has generated a unique URL for their to-do lists
		self.fail('Finish the test!')
		
		#The user visits the URL and sees that the to-do list is still there
		
		#END

if __name__ == '__main__':
	unittest.main(warnings='ignore')
		


