from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Chrome driver
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

# print("title", driver.title)

# Find the search box and perform a search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# print("title", driver.title)

search_result = driver.find_element(By.ID, "search")

# print("search results", search_result.text)

# print("page source", driver.page_source)

# driver.implicitly_wait(2)
try:
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "MjjYud"))
    )
    results = search_result.find_elements(By.CLASS_NAME, "MjjYud")
    for result in results:
        # print("result href", result.get_attribute("href"))
        # print("result", result.)
        link = result.find_element(By.CSS_SELECTOR, "a")
        # print("link ", link.get_attribute("href"))
        # print("link html", link.get_attribute("outerHTML"))
        print(
            f"Text: {link.find_element(By.CSS_SELECTOR,'h3').text}, Link: {link.get_attribute('href')}"
        )
except:
    print("element not found")
    # driver.quit()

# time.sleep(5)

# element = driver.find_element(By.CLASS_NAME, "content__CardContentTitle-sc-1nrnigk-3")
# elements = driver.find_elements(By.CLASS_NAME, "tag__TagContainer-sc-3f52y0-0")
# # print("element", element.text)
# for element in elements:
#     # element.get_attribute("href")
#     # print("element text", element.text)
#     print(f"Text: {element.text}, Href: {element.get_attribute('href')}")
