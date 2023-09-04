from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

"""lang_selector = driver.find_element(By.ID,"langSelect-EN")
lang_selector.click()

cookie = driver.find_element(By.ID,"bigCookie")



actions.click(cookie)

for i in range(5000):
    actions.perform()"""
    
actions = ActionChains(driver)

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"langSelect-EN"))
    )
    element.click()

    cookie_count= WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"cookies"))
    )

    items = [driver.find_element(By.ID,"productPrice" + str(i))for i in range(1,-1,-1)]

    cookie = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"bigCookie")),          
    )
    #actions.click(cookie) 
    for i in range(1000):
        actions.click(cookie)
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

finally:
    driver.quit()



#cookie = driver.find_element(By.ID,"bigCookie")
#cookie_count = driver.find_element(By.ID,"cookies")

#items = [driver.find_element(By.ID,"productPrice" + str(i))for i in range(1,-1,-1)]




