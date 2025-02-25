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