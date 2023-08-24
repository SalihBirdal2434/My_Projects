from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj) 


driver.get("https://www.lcwaikiki.com/tr-TR/TR")


#relative Xpath
#driver.find_element(By.XPATH,"//input[@id='search-form__input-field__search-input']").send_keys("Tişört")#relative xpath
#driver.find_element(By.XPATH,"//button[@type='button']").click()

#ABs XPath

driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/header[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Tişört")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/header[1]/div[2]/div[2]/form[1]/div[1]/div[2]/button[1]").click()



time.sleep(10)









































