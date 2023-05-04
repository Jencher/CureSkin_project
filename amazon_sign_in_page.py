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

expected_result_1 = "Sign in"
actual_result_1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result_1 == actual_result_1, f'Error! Expected {expected_result_1} bot got actual {actual_result_1}'

expected_result_2 = driver.find_element(By.ID,'ap_email')
actual_result_2 = driver.find_element(By.ID,'ap_email')
assert expected_result_2 == actual_result_2, f'Error! Expected {expected_result_2} bot got actual {actual_result_2}'


print('Test case passed!')

driver.quit()