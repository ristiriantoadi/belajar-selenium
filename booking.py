import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.booking.com/")

try:
    buttonClosePopUpSignIn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[aria-label="Dismiss sign-in info."]')
        )
    )
    buttonClosePopUpSignIn.click()
except:
    pass


changeCurrencyButton = driver.find_element(
    By.CSS_SELECTOR,
    ".bf33709ee1.a190bb5f27.dc0e35d124.bb5314095f.b81c794d25.b24dc6cf0f",
)
changeCurrencyButton.click()


USDCurrencyButton = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(., 'USD')]"))
)
USDCurrencyButton.click()

WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "ad82e69f7d"), "USD")
)

occupancyConfigButton = driver.find_element(
    By.CSS_SELECTOR, '[data-testid="occupancy-config"]'
)
occupancyConfigButton.click()

adultMinusButton = driver.find_element(
    By.CLASS_NAME,
    "becc918b37",
)
adultMinusButton.click()

try:
    petsCheckbox = driver.find_element(By.CLASS_NAME, "dab8ed599c")
    if petsCheckbox.is_selected() is False:
        petsCheckbox.click()
except:
    pass


# occupancyPopUp = driver.find_element(By.CSS_SELECTOR, '[data-testid="occupancy-popup"]')
# print("occupancyPopUp.location['x']", occupancyPopUp.location["x"])
# driver.execute_script(
#     f"document.elementFromPoint({occupancyPopUp.location['x'] + occupancyPopUp.size['width'] + 20}, {occupancyPopUp.location['y'] + occupancyPopUp.size['height'] + 20}).click();"
# )

doneButton = driver.find_element(By.XPATH, "//button[contains(., 'Done')]")
doneButton.click()

destinationInput = driver.find_element(By.NAME, "ss")
destinationInput.send_keys("Jakarta")
WebDriverWait(driver, 3).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "a3b830f8ca"), "Jakarta")
)
destinationOption = driver.find_element(By.CLASS_NAME, "a3b830f8ca")
destinationOption.click()

searchButton = driver.find_element(By.XPATH, "//button[contains(., 'Search')]")
searchButton.click()

# driver.find_element(By.XPATH, "//html").send_keys(Keys.TAB)
# driver.find_element(By.XPATH, "//html").send_keys(Keys.ENTER)

# Actions action = new Actions(driver);
# action.moveByOffset(0, 0).click().build().perform();
# driver.find_element(By.XPATH, "//html").send_keys(Keys.TAB)
# ActionChains(driver).move_by_offset(10, 10).click().perform()
# driver.get(driver.current_url)
# driver.find_element(By.CLASS_NAME, "b290e5dfa6").click()

# driver.find_element(By.XPATH, "//button[contains(., 'Skip to main content')]").click()


# ActionChains(driver).move_by_offset(0, 0).click().perform()

destinationInput = driver.find_element(By.NAME, "ss")
destinationInput.click()

while True:
    time.sleep(100)

# # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tutorials")))
# buttonUSD = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//button[contains(., 'USD')]"))
# )

# # buttonUSD = driver.find_element(By.XPATH, "//button[contains(., 'USD')]")
# buttonUSD.click()

# time.sleep(5)
