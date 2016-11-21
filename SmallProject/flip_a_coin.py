from selenium import webdriver
import time

driver = webdriver.Chrome()

# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
print (driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("Google in 1998")
inputElement.submit()

time.sleep(3)

inputElement = driver.find_element_by_name("q")
inputElement.send_keys("flip a coin")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

time.sleep(5)
driver.quit()