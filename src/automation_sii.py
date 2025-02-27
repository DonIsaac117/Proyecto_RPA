from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Conectar a Chrome en modo depuración
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"

driver = webdriver.Chrome(options=chrome_options)

# Abrir la página
driver.execute_script("window.open('https://sii.confecamaras.co/vista/plantilla/index.php', '_blank');")
time.sleep(2)  # Esperar carga

# Cambiar a la pestaña de SII
driver.switch_to.window(driver.window_handles[-1])

wait = WebDriverWait(driver, 10)

# **1. Seleccionar Cámara de Comercio**
camara = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#camara_47")))
camara.click()
time.sleep(2)  # Esperar a que cargue la página del login

# **2. Intentar ingresar usuario**
try:
    campo_usuario = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mail")))

    # **Forzar que el campo sea interactuable**
    driver.execute_script("arguments[0].style.display = 'block';", campo_usuario)  # Hacer visible
    driver.execute_script("arguments[0].removeAttribute('readonly');", campo_usuario)  # Quitar restricciones
    driver.execute_script("arguments[0].focus();", campo_usuario)  # Enfocar

    # **Borrar y escribir usuario**
    campo_usuario.clear()
    campo_usuario.send_keys("basesdat")
    print("✅ Usuario ingresado correctamente.")

except Exception as e:
    print("❌ Error al ingresar el usuario:", str(e))

# **3. Intentar ingresar identificación**
try:
    campo_identificacion = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identificacion")))
    campo_identificacion.clear()
    campo_identificacion.send_keys("11431332")  # Cambia por la identificación real
    print("✅ Identificación ingresada correctamente.")

except Exception as e:
    print("❌ Error al ingresar la identificación:", str(e))

# **4. Intentar ingresar contraseña**
try:
    campo_contraseña = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pass")))
    driver.execute_script("arguments[0].focus();", campo_contraseña)
    campo_contraseña.clear()
    campo_contraseña.send_keys("CT6Z69BT")
    print("✅ Contraseña ingresada correctamente.")
    

except Exception as e:
    print("❌ Error al ingresar la contraseña:", str(e))

# **5. Esperar al CAPTCHA (si es necesario)**
# input("Si aparece CAPTCHA, resuélvelo y presiona ENTER para continuar...")

# **6. Clic en el botón de inicio de sesión**
try:
    boton_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#formLogin > div:nth-child(6) > div > button")))
    boton_login.click()
    print("✅ Inicio de sesión completado.")

except Exception as e:
    print("❌ Error al hacer clic en el botón de inicio de sesión:", str(e))

time.sleep(6) 
# 1. Clic en el botón del menú lateral para expandirlo
try:
    menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#expMenu > a > span > i")))
    driver.execute_script("arguments[0].scrollIntoView();", menu)  # Asegurar que sea visible
    menu.click()
    print("✅ Menú de navegación abierto.")
    time.sleep(4)  # Dar tiempo a la animación del menú

except Exception as e:
    print("❌ Error al abrir el menú de navegación:", str(e))

# Verificar si el botón de registros está presente
time.sleep(2)  # Pequeña espera para que cargue el DOM
registros_lista = driver.find_elements(By.CSS_SELECTOR, "#accordionLateral1 > div > li > a")

# Imprimir los botones encontrados
for i, r in enumerate(registros_lista):
    print(f"🔎 Botón {i+1}: {r.text}")

# Intentar hacer clic
try:
    registros = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#accordionLateral1 > div:nth-child(3) > li > a")))
    registros.click()
    print("✅ Opción 'Registros' seleccionada.")
    time.sleep(3)

except Exception as e:
    print("❌ Error al hacer clic en 'Registros':", str(e))

