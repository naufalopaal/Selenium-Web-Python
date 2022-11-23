from behave import *



# dependency
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from chromedriver_py import binary_path # this will get you the path variable


# service_object = Service(binary_path)
# driver = webdriver.Chrome(service=service_object)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@given(u'User go to secondhand website')
def step_impl(context):
    context.browser = webdriver.Chrome(executable_path=r"C:\Users\User\Desktop\DriverChrome\chromedriver.exe",options=options) #use chrome driver
    context.browser.get("https://secondhand-store.herokuapp.com/login")
    

@when(u'User input email {email}')
def step_impl_input_email(context, email):
     context.browser.find_element(By.XPATH,'//*[@id="exampleInputEmail1"]').send_keys(email)


@when(u'User input password {password}')
def step_impl_User_input_password(context, password):
    context.browser.find_element(By.XPATH,'//*[@id="exampleInputPassword1 "]').send_keys(password)


@when(u'User click Masuk button')
def step_impl(context):
    context.browser.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/form/button').click()


@then(u'User successfully login')
def step_impl(context):
    time.sleep(4)
