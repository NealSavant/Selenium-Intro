import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

################################################################################################
# Setup
################################################################################################
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# Install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get("https://github.com/NealSavant?tab=repositories")
driver.implicitly_wait(1)
################################################################################################


# Find repository. Pass the repository number out of the total
def get_repository(count):
    repo_list = driver.find_element(By.ID, 'user-repositories-list')
    repo_names = repo_list.find_elements(By.CLASS_NAME, 'wb-break-all')
    return repo_names[count].find_element(By.TAG_NAME, 'a')

# Pull all Languages used in the Repository
def get_languages():
    return_list = []
    
    sidebar = driver.find_element(By.CLASS_NAME, 'Layout-sidebar')
    sidebar_boxes = sidebar.find_elements(By.CLASS_NAME, 'BorderGrid-row')
    language_box = sidebar_boxes[-1]
    # Verify this is the language box
    try:
        if language_box.find_element(By.CLASS_NAME, 'h4.mb-3').accessible_name != 'Languages':
            return None
    except:
        return None

    language_list = language_box.find_element(By.TAG_NAME, 'ul')
    language_elements = language_list.find_elements(By.XPATH, "//span[@class='color-fg-default text-bold mr-1']")
    for language_box in language_elements:
        return_list.append(language_box.get_attribute('innerHTML'))

    return return_list

############################################################################################################
# Main
############################################################################################################

# Check how many repositories we will need to loop through
repo_box = driver.find_element(By.XPATH, '//*[@id="user-repositories-list"]/ul')
repo_count = len(repo_box.find_elements(By.TAG_NAME, 'li')) # Count of repos to check
repository_language_list = [] # final data set

for i in range(repo_count):
    repo = get_repository(i)
    data = {
        "repo_name": repo.accessible_name
    }
    repo.click()
    time.sleep(1) # Wait for dom content to fully load
    languages= get_languages()
    data['languages'] = languages if languages else None
    repository_language_list.append(data)
    driver.back()


# Write to File
driver.close()
with open('results.json', 'w') as outfile:
    json.dump(repository_language_list, outfile)
# print(repository_language_list)

