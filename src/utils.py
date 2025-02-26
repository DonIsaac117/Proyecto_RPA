from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager        
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pyperclip
#"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\SOPORTETI\AppData\Local\Google\Chrome\User Data"

# Ruta del driver descargado manualmente
ruta_driver = "C:\\chromedriver-win64\\chromedriver.exe"

# Opciones de Chrome para modo depuración
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"  # Se conecta a Chrome en modo depuración

# Conectar solo a la sesión abierta
driver = webdriver.Chrome(options=chrome_options)

print ("conexion exitosa")

print(pyautogui.position())