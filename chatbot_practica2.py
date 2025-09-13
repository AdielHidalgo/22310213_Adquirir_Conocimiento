# Importamos librerías necesarias
import json   # Sirve para guardar y cargar la base de conocimiento en formato JSON (un formato tipo diccionario)
import os     # Sirve para verificar si existe el archivo donde guardamos el conocimiento

# Nombre del archivo donde se guardará la base de conocimiento
ARCHIVO = "conocimiento.json"

# --- Cargar la base de conocimiento ---
# Si el archivo ya existe, lo abrimos y cargamos su contenido
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        base_conocimiento = json.load(f)  # Convierte el archivo JSON en un diccionario de Python
else:
    # Si no existe el archivo, creamos una base de conocimiento inicial (3 frases precargadas)
    base_conocimiento = {
        "hola": "¡Hola! ¿Cómo estás?",
        "como estas": "Estoy bien, gracias. ¿Y tú?",
        "de que te gustaria hablar": "Podemos hablar de lo que quieras."
    }

print("=== Chatbot - Sistema Experto Básico ===")
print("Escribe 'salir' para terminar.\n")

# --- Ciclo principal del chatbot ---
while True:
    entrada = input("Tú: ").lower().strip()  # Convertimos a minúsculas y quitamos espacios extra

    if entrada == "salir":
        print("Chatbot: ¡Adiós! Hasta la próxima.")
        break

    # Si la entrada ya está en la base de conocimiento → responde
    if entrada in base_conocimiento:
        print("Chatbot:", base_conocimiento[entrada])
    else:
        # Si no sabe la respuesta, entra en modo adquisición de conocimiento
        print("Chatbot: No sé cómo responder a eso.")
        nueva_respuesta = input("¿Qué debería contestar cuando digas eso?: ")

        # Guardamos la nueva respuesta en la base de conocimiento (diccionario en memoria)
        base_conocimiento[entrada] = nueva_respuesta

        # También lo guardamos en el archivo JSON para que no se pierda al cerrar
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(base_conocimiento, f, indent=4, ensure_ascii=False)

        print("Chatbot: ¡Gracias! He aprendido algo nuevo.")
