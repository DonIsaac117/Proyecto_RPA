from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Conectar a Chrome en modo debug
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=chrome_options)

# Obtener todas las pestañas abiertas antes de abrir una nueva
tabs_before = driver.window_handles  

# Cambiar a la última pestaña abierta actualmente
driver.switch_to.window(tabs_before[-1])

# Abrir una nueva pestaña para Outlook
driver.execute_script("window.open('https://outlook.office.com/mail/', '_blank');")

# Esperar un momento para que la nueva pestaña se cree
import time
time.sleep(2)

# Obtener todas las pestañas abiertas después de abrir Outlook
tabs_after = driver.window_handles 

if len(tabs_after) > len(tabs_before):
    nueva_pestaña = list(set(tabs_after) - set(tabs_before))[0]  
    driver.switch_to.window(nueva_pestaña)  
    print("Se abrió Outlook en la nueva pestaña.")
else:
    print("Error: No se encontró la nueva pestaña de Outlook.")

# Obtener todas las pestañas nuevamente
for idx, tab in enumerate(tabs_after):
    driver.switch_to.window(tab)  # Cambiar a cada pestaña
    print(f"{idx}: {tab} - {driver.title}")  # Mostrar su título

driver.switch_to.window(tabs_after[-1])  # Cambiar a la pestaña de Outlook
print("Pestaña activa:", driver.title)  

wait = WebDriverWait(driver, 4)  # Aumentamos a 30 segundos

# Opción 1: Esperar por el título de Outlook
wait.until(EC.title_contains("Correo: Jorge Isaac Espitia Cardozo - Outlook"))

# Opción 2: Esperar por la bandeja de entrada
nuevo_mensaje = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Correo nuevo']/ancestor::button")))
nuevo_mensaje.click()

# Campo "Para" (destinatario)
campo_destinatario = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox' and @aria-label='Para']")))
campo_destinatario.send_keys("correo@ejemplo.com")

# Escribir el asunto
campo_asunto = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Agregar un asunto']")))
campo_asunto.send_keys("Asunto de prueba")

campo_cuerpo = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']")))
campo_cuerpo.click()  # Activa el campo
campo_cuerpo.send_keys("Este es el contenido del correo.")









