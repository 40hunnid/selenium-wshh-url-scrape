#--------Here im going to click on the link and grab the URL / put ULR in variable
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\Owner\\Downloads\\chromedriver_win32\\chromedriver.exe")
#--------This is an example of what im searching in WSHH. Im searching: fight
#--------IF YOU WANT TO CHANGE WHAT YOUR SEARCHING CHANGE "FIGHT" TO WHATEVER
driver.get("https://worldstarhiphop.com/videos/search.php?s=fight")
time.sleep(1.5)
current_title = driver.find_elements_by_class_name("title")


#--------The code below will grab the URL of the most recent post
newList = driver.find_element(By.XPATH, '/html/body/div/div/main/section/div/section/section[1]')
newList.click()
time.sleep(1.5)
print("current url:", driver.current_url)
wshhURL = driver.current_url
time.sleep(1)
driver.back()
time.sleep(0.5)

#-----------Entering tube offline site
driver.get("https://www.tubeoffline.com/download-WorldstarHipHop-videos.php")
tubeOffline = driver.find_element_by_id("video")
tubeOffline.send_keys(wshhURL)
time.sleep(0.5)

#----------Clicking search
searchButton = driver.find_element_by_id("submitbutton")
searchButton.click()

#From here you guys can implement the rest of the download code if your farmiliar
#With selenium, this is just an example. There are many ways. 
