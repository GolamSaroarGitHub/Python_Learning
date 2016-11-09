from selenium import webdriver
import getpass



driver = webdriver.Firefox()
# print('Enter the facebook user name: \n')
# user=input()
# print('Enter the facebook password \n')
# password=getpass.getpass()
driver.set_page_load_timeout(120)
driver.get('https://demo.testreach.com')
driver.maximize_window()
driver.implicitly_wait(20)



# driver.get_screenshot_as_file("screenshots\\facebook.png")
driver.find_element_by_id("username-field").send_keys("golamsaroar89+1@gmail.com")
driver.find_element_by_name("password").send_keys("123")
# driver.find_element_by_id("u_0_l").click()
# driver.get_screenshot_as_file("screenshots\\facebook1.png")
############Executing Javascript inline##############
element = driver.execute_script("return $('button')[0]")
# driver.find_element_by_tag_name("button").click()
element.click()