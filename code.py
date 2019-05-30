#This example was made for a senior who was peer pressured to tell every junoir to fill up a form.
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('directory/to/your/chromedriver') 
driver.get('https://mycutebaby.in/contest/participant/?n=5cc1a364c4e7c')
#HTML is a xml language. Basicly I used xpath of the element to find the element(https://selenium-python.readthedocs.io/locating-elements.html)
button= driver.find_element_by_xpath("//button[@onclick='getLocation()']")
button.send_keys(Keys.RETURN)
time.sleep(10) # Let you people actually see something!
#name=driver.find_element_by_xpath("//*[@id='v']")
#name.send_keys('Dhruv')
button2=driver.find_element_by_xpath("//*[@id='vote_btn']")
button2.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
#The End