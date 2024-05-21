from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

for b in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    sleep(2)
    button.click()
    driver.refresh()

driver.quit()
