from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://secondhand-store.herokuapp.com/login")
time.sleep(1)
#driver.find_element(By.XPATH,"//*[@id='details-button']").click()

#login
username = "binarqae1@gmail.com"
password = "students1234"
driver.find_element(By.XPATH,'//*[@id="exampleInputEmail1"]').send_keys(username)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="exampleInputPassword1 "]').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/form/button').click()
time.sleep(4)