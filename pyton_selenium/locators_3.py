from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



serv_obj=Service("C:\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window() #maximize the window

#tag and id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("salih.birdal@hotmail.com")
#driver.find_element(By.CSS_SELECTOR,"email").send_keys("salih.birdal@hotmail.com")


#tag(optional) and class

#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")#the facebook input name has a some of space value
#this is a problem because of error.In solution we can use only some of keys!! 

#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

#tag & attribute combination 
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("salih")
#driver.find_element(By.CLASS_NAME,"[data-testid=royal_email]").send_keys("salih")


#tag,class & attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc.com")#the facebook input name has a some of space value








time.sleep(10)















