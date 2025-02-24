from selenium import webdriver

# Conectar a Chrome en modo debug
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=chrome_options)

# Obtener todas las pestañas abiertas antes de abrir una nueva
tabs_before = driver.window_handles  

# Cambiar a la última pestaña abierta actualmente
driver.switch_to.window(tabs_before[0])

# Abrir una nueva pestaña para Outlook
driver.execute_script("window.open('https://outlook.office.com/mail/', '_blank');")

# Esperar un momento para que la nueva pestaña se cree
import time
time.sleep(1)

# Obtener todas las pestañas abiertas después de abrir Outlook
tabs_after = driver.window_handles  

# Identificar la nueva pestaña (debe ser la última)
if len(tabs_after) > len(tabs_before):
    driver.switch_to.window(tabs_after[-1])  # Cambiamos a la nueva pestaña
    print("Se abrió Outlook en la última pestaña.")
else:
    print("Error: No se encontró la nueva pestaña de Outlook.")