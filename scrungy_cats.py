import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from urllib.request import urlretrieve

################################################################################################
# Setup
################################################################################################
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# Install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get("https://www.reddit.com/r/scrungycats/top/?t=all")
driver.implicitly_wait(1)
################################################################################################
count = 0
while(count < 5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    count += 1
    time.sleep(.5)

images = driver.find_elements(By.CSS_SELECTOR, "img[alt='Post image']")

for i, img in enumerate(images):
    src = img.get_attribute('src')
    if "external-preview" in src:
        continue
    urlretrieve(src, "./cats2/cat%s.png"% i)



# Write to File
driver.close()
# with open('results.json', 'w') as outfile:
#     json.dump(repository_language_list, outfile)
# print(repository_language_list)

