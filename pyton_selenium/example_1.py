"""chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)"""





#Test Case 
#------------
#Open a web browser
#Open URL https://opensource-demo.orangehrmlive.com/
#Enter Username
#Enter Password
#Click on login
#Capture title of home page(Actual Title)
#Verify title of the page:OrangwHrm (Excepted)
#Close browser


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://www.facebook.com/')


driver.find_element(By.ID,"email").send_keys("salih-birdal@hotmail.com")
driver.find_element(By.ID,"pass").send_keys("Slhbrdl123")
driver.find_element(By.NAME,"login").click()

act_title=driver.title
exp_title="(20+) Facebook"

if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test ")
time.sleep(10)













