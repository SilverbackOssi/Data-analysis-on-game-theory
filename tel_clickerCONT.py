
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import time
import importlib
clicker = importlib.import_module("clickerMAIN")
#initialize webdriver on private browsing mode
options = Options()
options.add_argument("inprivate")
web_driver = webdriver.Edge(options = options)

# get result page URL
url = 'https://web.telegram.org/a/'
web_driver.get(url) 
web_driver.maximize_window()
time.sleep(60)
# wait for page to load 
  
content_is_visible = WebDriverWait(web_driver,1800).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Tab_inner")))

while True: 
    print("refreshing")   
    importlib.reload(clicker)
    time.sleep(5)
    clicker.main(web_driver)
    if clicker.status == "kill":
        break
web_driver.quit()
print("done, quitting...")