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

# Obtener todas las pestañas abiertas antes de abrir una nueva
tabs_before = driver.window_handles  

# Cambiar a la última pestaña abierta actualmente
driver.switch_to.window(tabs_before[-1])

# Abrir una nueva pestaña para Outlook
driver.execute_script("window.open('https://outlook.office.com/mail/', '_blank');")

# Esperar un momento para que la nueva pestaña se cree

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

# Abrir un nuevo correo
nuevo_mensaje = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Correo nuevo']/ancestor::button")))
nuevo_mensaje.click()

# Campo "Para" (destinatario)
campo_destinatario = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox' and @aria-label='Para']")))
campo_destinatario.send_keys("correo@ejemplo.com")

# Campo "CC"
campo_cc = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='CC']")))
campo_cc.click()
campo_cc.send_keys("cc@example.com")

# **Forzar cambio de foco** haciendo clic en el campo "Asunto"
campo_asunto = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Agregar un asunto']")))
campo_asunto.click()
campo_asunto.send_keys("Asunto de prueba")
time.sleep(2)

# **Esperar a que el cuerpo del correo esté presente y activarlo**
campo_cuerpo = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'elementToProof')]")))
campo_cuerpo.click()
campo_cuerpo.send_keys("Este es el contenido del correo.")



# Hacer clic en el botón "Adjuntar"
boton_adjuntar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Adjuntar')]")))
boton_adjuntar.click()
time.sleep(2)

# Hacer clic en "Examinar este equipo"
boton_examinar = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Examinar este equipo']")))
boton_examinar.click()
time.sleep(2)  # Pausa para que se abra la ventana del explorador

print("Esperando la ventana de selección de archivos...")
time.sleep(2)  # Asegurar que la ventana se haya abierto correctamente

# **Forzar el foco en la ventana emergente**
pyautogui.click(x=377, y=69)  # Clic en el centro de la pantalla (ajustar si es necesario)
time.sleep(1)

# **Método alternativo: Escribir la ruta directamente en lugar de pegarla**
ruta_archivo = r"C:\Users\SOPORTETI\Downloads\Lorem ipsum dolor sit amet.pdf"
print("Escribiendo la ruta del archivo...")
pyautogui.write(ruta_archivo)  # Escribir la ruta directamente
time.sleep(1)

print("Presionando ENTER para seleccionar el archivo...")
pyautogui.press("enter")  # Confirmar selección del archivo
time.sleep(2)

print("Archivo adjuntado correctamente.")
