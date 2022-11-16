from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"./Driver/chromedriver")
driver.get("http://localhost:3000")
print("Found the website!")

testname = "Teszt Elek"
testpassword = "12345"
testage = "23"

driver.maximize_window()
print("Finding form elements...")
driver.find_element(By.ID,"name").send_keys("Teszt Elek")
print("Found the name field and entered test name")
driver.find_element(By.ID,"password").send_keys("12345")
print("Found the password field and entered test password")
driver.find_element(By.ID,"age").send_keys("23")
print("Found the age field and entered test age")
driver.find_element(By.ID, "submitform1").send_keys(Keys.ENTER)
print("Successfully submitted form!")

driver.implicitly_wait(10)

returnedName = driver.find_element(By.ID, "nameReturn").text
print(returnedName)

assert returnedName == testname

