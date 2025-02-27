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
campo_destinatario.send_keys("soporte@ccfacatativa.org.co")

# Campo "CC"
campo_cc = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='CC']")))
campo_cc.send_keys("soporte@ccfacatativa.org.co")

# **Forzar cambio de foco** haciendo clic en el campo "Asunto"
campo_asunto = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Agregar un asunto']")))
campo_asunto.send_keys("Asunto de prueba")
time.sleep(1)

# **Esperar a que el cuerpo del correo esté presente y activarlo**
campo_cuerpo = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @aria-label='Cuerpo del mensaje, presione Alt+F10 para salir']")))
campo_cuerpo.click()
campo_cuerpo.send_keys("Este es el contenido del correo.")

ruta_archivo = r"C:\Users\SOPORTETI\Downloads\Lorem ipsum dolor sit amet.pdf"

# Busca todos los inputs de tipo file
inputs_adjuntar = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))

# Si hay más de un input, selecciona el segundo (índice 1)
if len(inputs_adjuntar) > 1:
    inputs_adjuntar[1].send_keys(ruta_archivo)
else:
    print("No se encontró el input de adjuntar archivos correcto.")

# Esperar hasta que al menos un archivo adjunto aparezca en la lista
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox' and @aria-label='archivos adjuntos']//div[@role='option']")))

# Ahora sí, hacer clic en el botón de enviar
boton_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar']")))
boton_enviar.click()




