import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Chrome driver
driver = webdriver.Chrome()

# driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.get(
    "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
)
# firstName = driver.find_element(By.NAME, "firstname")
# firstName.send_keys("Something")

# male = driver.find_element(By.ID, "sex-0")
# driver.execute_script("arguments[0].scrollIntoView(true);", male)
# male.click()

# female = driver.find_element(By.ID, "sex-1")
# # driver.execute_script("arguments[0].scrollIntoView(true);", female)
# female.click()

# professionO = driver.find_element(By.ID, "profession-0")
# driver.execute_script("arguments[0].scrollIntoView(true);", professionO)
# if professionO.is_selected() is False:
#     professionO.click()
# dropdown = Select(driver.find_element(By.ID, "continents"))
# driver.execute_script(
#     "arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "continents")
# )
# # print("options", dropdown.all_selected_options)
# dropdown.select_by_visible_text("South America")
# selected_option = dropdown.first_selected_option.text
# print("Selected option:", selected_option)

# loginMenuButton = driver.find_element(By.XPATH, "//a[text()='Login']")
loginMenuButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Login')]"))
)
print(loginMenuButton.text)

time.sleep(20)
