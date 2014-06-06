from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
		
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#ida visits homepage
		self.browser.get(self.live_server_url)

		#ida looks at page title and heading
		self.assertIn('To-Do', self.browser.title)
		
		#ida invited to enter to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		#ida types "Buy peacock feathers" into text box
		inputbox.send_keys('Buy peacock feathers')

		#when ida hits enter, the page updates, and the page lists "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		
		ida_list_url = self.browser.current_url
		self.assertRegex(ida_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		#There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to be stupid')
		inputbox.send_keys(Keys.ENTER)

		#The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to be stupid')
		
		#Now a new user, Peter, visits
		
		## Use a new browser session to make sure Ida's session is over
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		# Peter hits the homepage and there is no trace of Ida's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
		
		# Peter starts a new list by entering a new item
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		
		# Peter gets his own unique URL
		peter_list_url = self.browser.current_url
		self.assertRegex(peter_list_url, '/lists/.+')
		self.assertNotEqual(peter_list_url, ida_list_url)
		
		# Again, there is no trace of ida's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
						
		#The user sees that the site has generated a unique URL for their to-do lists
		self.fail('Finish the test!')
		
		#The user visits the URL and sees that the to-do list is still there
		
		#END
		


