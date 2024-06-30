import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Chrome driver
driver = webdriver.Chrome()

driver.get("https://www.techwithtim.net/")

# tutorialLink = driver.find_element(By.LINK_TEXT, "Tutorials")
tutorialLink = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Tutorials"))
)


# print("tutorial", tutorialLink.get_attribute("outerHTML"))

# driver.execute_script("arguments[0].scrollIntoView(true);", tutorialLink)
# # print("tutorial", tutorialLink.get_attribute("href"))
# tutorialLink.click()


driver.execute_script("arguments[0].click();", tutorialLink)

tutorials = driver.find_elements(
    By.CLASS_NAME, "tutorial__TutorialCardContainer-sc-1rebzxr-0"
)


for index in range(len(tutorials)):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tutorials[index]))
    tutorials[index].click()
    print("current url", driver.current_url)
    driver.back()
    tutorials = driver.find_elements(
        By.CLASS_NAME, "tutorial__TutorialCardContainer-sc-1rebzxr-0"
    )

time.sleep(3)
