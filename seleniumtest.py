from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()

chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

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
driver.find_element(By.XPATH, "//*[@id='submitform1']").send_keys("\n")
time.sleep(3)
print("Successfully submitted form!")

driver.implicitly_wait(10)

returnedName = driver.find_element(By.XPATH,"//*[@id='nameReturn']").text
returnedPass = driver.find_element(By.XPATH,"//*[@id='passReturn']").text
returnedAge = driver.find_element(By.XPATH,"//*[@id='ageReturn']").text
print("Successfully gathered form returns")
#print(returnedName)

print("## Testing Form 1 now")

print("Testing returned form name")
assert returnedName == testname
print("### Test Successful: Successful return of name")

print("Testing returned form password")
assert returnedPass == testpassword
print("### Test Successful: Successful return of password")

print("Testing returned form age")
assert returnedAge == testage
print("### Test Successful: Successful return of age")
print()
print("## Form 1 tests ended successfully!")
print()

print("## Testing Calcform now")
driver.find_element(By.XPATH, "//*[@id='num1']").send_keys("12")
print("Found num1 and entered 12")
driver.find_element(By.XPATH, "//*[@id='num2']").send_keys("3")
print("Found num 2 and entered 3")
driver.find_element(By.XPATH, "//*[@id='num3']").send_keys("12")
print("Found num1 and entered 12")
driver.find_element(By.XPATH, "//*[@id='num4']").send_keys("3")
driver.find_element(By.XPATH, "//*[@id='submitcalcform']").send_keys(Keys.ENTER)
#driver.find_element(By.XPATH, "//*[@id='submitcalcform']").submit()
time.sleep(3)
print("Found and clicked form button")

element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "additionResult"))
        )
#print(element)

ResultofAddition = driver.find_element(By.XPATH, "//*[@id='additionResult']").text
print("Found and retrieved valuee from addition result")

#print(ResultofAddition.get_attribute('value'))

ResultofSubtraction = driver.find_element(By.XPATH, "//*[@id='subtractionResult']").text

print("Testing result of addition...")
assert ResultofAddition == "15"
print("### Test Successful: Successful return of addition")

print("Testing result of subtraction...")
assert ResultofSubtraction == "9"
print("### Test Successful: Successful return of subtraction")

print()
print("## Calcform tests ran successfully")

print("#####################################")
print("All tests ran successfully!")

driver.quit()

