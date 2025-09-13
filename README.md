📚 Explicación de librerías usadas:

json:
Sirve para trabajar con archivos en formato JSON (JavaScript Object Notation), que es muy usado en empresas y proyectos porque es ligero y fácil de leer.

json.load() → convierte el archivo JSON en un diccionario de Python.

json.dump() → guarda el diccionario en un archivo JSON.

os:
Nos ayuda a interactuar con el sistema operativo.

os.path.exists(ARCHIVO) → revisa si ya existe el archivo conocimiento.json antes de intentar abrirlo.

👉 Así, el chatbot tiene:

Módulo de conocimiento inicial (3 frases).

Adquisición de conocimiento (aprende nuevas respuestas).

Persistencia en archivo JSON (recuerda lo aprendido aunque cierres el programa).
