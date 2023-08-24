from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



serv_obj=Service("C:\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() #maximize the window


#id&name locators
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#linktext & partial linktext
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

#sliders=driver.find_elements(By.CLASS_NAME,"salih")
#print(len(sliders)) => total number of sliders on home page


links=driver.find_elements(By.TAG_NAME,"a")
print(len(links)) #total number of links on home page

"""If we didin'f find Id or Name parameteres,we should find other alternatives.PARTİAL LINK TEST"""
time.sleep(10)























