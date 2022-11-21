from behave import *
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@given(u'User go to secondhand website')
def step_impl(context):   
    context.browser = webdriver.Chrome()
    context.browser.get("https://secondhand-store.herokuapp.com/login")
    

@when(u'User input email {email}')
def step_impl_input_email(context, email):
    #  context.browser = webdriver.Chrome()
     context.browser.find_element(By.XPATH,'//*[@id="exampleInputEmail1"]').send_keys(email)


@when(u'User input password {password}')
def step_impl_User_input_password(context, password):
    # context.browser = webdriver.Chrome()
    context.browser.find_element(By.XPATH,'//*[@id="exampleInputPassword1 "]').send_keys(password)


@when(u'User click Masuk button')
def step_impl(context):
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/form/button').click()


@then(u'User successfully login')
def step_impl(context):
    time.sleep(4)
