from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

driver.get(
    "https://www.namecheap.com/blog/introducing-simple-links-easy-links-in-bio-pages/"
)

tutorialLink = driver.find_element(By.LINK_TEXT, "Simple Links")
tutorialLink.click()
