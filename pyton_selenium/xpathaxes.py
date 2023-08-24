from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("C:\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.ntv.com.tr/istanbul-hava-durumu")
driver.maximize_window()

time.sleep(5)


msg=driver.find_element(By.XPATH,"//div[@class='dygtag-masthead dygtag-decorator dygtag-decorator-masthead dygtag-decorator-filled']").text()
print(msg)
time.sleep(5)





