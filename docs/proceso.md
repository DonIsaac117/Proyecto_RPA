# 📌 Proceso del Funcionamiento del Programa

## 🔹 1. Recepción de Datos  
- El usuario ingresa los datos requeridos en la interfaz.  
- Al pulsar el botón **"Ejecutar"**, el programa inicia el proceso.  

## 🔹 2. Acceso al SII de Confecámaras  
- Se abre el navegador y se accede a la página del SII.
- Se verifica en el correo que no se haya solicitado una contraseña en el mismo dia.
- Se inicia sesión con el usuario y contraseña.
- Si es necesario, se solicita una nueva contraseña.  

    ### 🔸 2.1. Solicitud de Nueva Contraseña (si aplica)  
    - Se ingresa al correo electrónico.  
    - Se localiza el correo del SII con la nueva contraseña.  
    - Se extrae la clave y se usa para iniciar sesión.  

## 🔹 3. Extracción de Matriculados  
- Dentro del sistema, se ubica la opción de extracción de matriculados.  
- Se diligencian los campos requeridos y especificos según la información ingresada.  
- Se genera el archivo de matriculados.  

## 🔹 4. Descarga y Renombrado del Archivo  
- Se espera la llegada del correo con el archivo generado.  
- Se descarga y se renombra el archivo adecuadamente.  

## 🔹 5. Extracción de Renovados  
- Se repite el proceso de extracción, pero ahora para los renovados.  
- Se diligencian los campos requeridos especificos según la información ingresada.  
- Se genera el archivo de renovados.  

## 🔹 6. Descarga y Renombrado del Archivo de Renovados  
- Se espera la llegada del correo con el archivo de renovados.  
- Se descarga y se renombra el archivo adecuadamente.  

## 🔹 7. Ejecución del Macro para Filtrar Datos  
- Se abre el archivo de **matriculados** y se ejecuta el macro.  
- Se filtran y organizan los registros según los parámetros establecidos.  
- Se genera un nuevo archivo con los datos procesados.  

## 🔹 8. Procesamiento del Archivo de Renovados  
- Se abre el archivo de **renovados** y se ejecuta el macro.  
- Se generan los registros finales de matriculados y renovados filtrados.  
- El archivo final se guarda en una carpeta específica.  

## 🔹 9. Organización y Almacenamiento  
- Se localiza la carpeta generada en el equipo.  
- Se mueve a la carpeta correspondiente según la fecha.  

## 🔹 10. Preparación del Correo para el Envío  
- Se abre el correo y se genera un nuevo mensaje.  
- Se establecen los destinatarios, asunto y descripción.  
- Se adjunta el archivo final con los datos procesados.  

    ### 🔸 10.1. Funcionalidad Adicional: Envío Automático  
    - Por defecto, el envío automático estará **desactivado** para permitir la revisión manual.  
    - Se agregará una opción en la interfaz principal para activar o desactivar el envío automático.  

---

### ✅ **Fin del Proceso**
