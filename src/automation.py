from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()  # ¡Ojo! Ya no se necesita `ChromeDriverManager().install()`
driver.get("https://www.google.com")

import time
time.sleep(5)
driver.quit()
