from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
"""
url = "http://ebravo.pk/classic/softwares?page=1"
driver = webdriver.Chrome()
driver.get(url)"""
"""
try:
    for i in range(1,31):
        title= WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,f"/html/body/div[4]/div/div[1]/div/div[3]/div/div[{i}]/a/div/div[2]/h6"))
        ).get_attribute("innerHTML")
        print(title)
        for j in range(1,4):
            element= WebDriverWait(driver,10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,f"/html/body/div[4]/div/div[1]/div/div[3]/div/div[{i}]/a/div/div[2]/div/div/div[{j}]"))
            ).get_attribute("innerHTML")
            print(element)

finally:
    driver.quit()
"""



for i in range(1,11):
    url = f"http://ebravo.pk/classic/softwares?page={i}"
    driver = webdriver.Chrome()
    driver.get(url)
    Softwares = {}

    softwares = driver.find_element(By.CSS_SELECTOR,"body > div.main > div > div.col-md-8.m-top > div")
    software = softwares.find_elements(By.XPATH,'/html/body/div[4]/div/div[1]/div/div[3]/div')

    for s in software:
        title = s.find_elements(By.TAG_NAME,"h6")
        added = s.find_elements(By.XPATH,'/html/body/div[4]/div/div[1]/div/div[3]/div/div[1]/a/div/div[2]/div/div/div[1]')
        viewed = s.find_elements(By.XPATH,'/html/body/div[4]/div/div[1]/div/div[3]/div/div[1]/a/div/div[2]/div/div/div[2]')
        downloaded = s.find_elements(By.XPATH,'/html/body/div[4]/div/div[1]/div/div[3]/div/div[1]/a/div/div[2]/div/div/div[3]')

        for t in title:
            title_1 = t.text
            #print(t.text)

            for a,v,d in zip(added,viewed,downloaded):
                added1,viewed1,downloaded1 = a.text,v.text,d.text
                Softwares[title_1] = [added1,viewed1,downloaded1]

                #print(a.text,v.text,d.text)
        #print(title.text,data.text)
        #print(s.text)
    #print(Softwares)
    with open(f"Softwares{i}.json","a") as file:
        json.dump(Softwares,file,indent=3,sort_keys=True)


