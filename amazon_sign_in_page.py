from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'nav-orders').click()

expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'

#Verify email field presented
assert driver.find_element(By.ID,'ap_email').is_displayed(), 'Email field not shown'


print('Test case passed!')

driver.quit()