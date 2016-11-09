from selenium import webdriver
import getpass



driver = webdriver.Chrome()
print('Enter the facebook user name: \n')
user=input()
print('Enter the facebook password \n')
password=getpass.getpass()
driver.set_page_load_timeout(30)
driver.get('http://www.facebook.com')
driver.maximize_window()
driver.implicitly_wait(20)



driver.get_screenshot_as_file("screenshots\\facebook.png")
driver.find_element_by_id("email").send_keys(user)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("u_0_l").click()
driver.get_screenshot_as_file("screenshots\\facebook1.png")



