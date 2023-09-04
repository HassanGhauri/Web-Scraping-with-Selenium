from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = webdriver.Chrome()
url = "http://ebravo.pk/classic/"
driver.get(url)
search = driver.find_element(By.CLASS_NAME,"navbar-toggle")
search.click()
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Softwares"))
    )
    element.click()
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"search-input2")),    
    )
    element.clear()
    element.send_keys("windows")
    element.send_keys(Keys.RETURN)
finally:
    driver.quit





time.sleep(5)
print(driver.title)
"""while(True):
    pass
"""