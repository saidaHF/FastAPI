#   Construyendo una API con FastAPI y Python

Tu objetivo es construir una API utilizando FastAPI que permita realizar operaciones CRUD (crear, leer, actualizar y eliminar) en una lista de usuarios.

##  Requisitos

- [X]   Debes utilizar FastAPI y Python 3.x.
- [X]   Crea una lista de usuarios en memoria utilizando una lista de diccionarios.
    - [X]    La estructura de un usuario debe contener los siguientes campos:
        - [X]    id (entero): identificador único del usuario.
        - [X]    nombre (cadena): nombre del usuario.
        - [X]    edad (entero): edad del usuario.
    - [X]    La API debe ser capaz de realizar las siguientes operaciones:
        - [X]    Obtener todos los usuarios.
        - [X]    Obtener un usuario por su ID.
        - [X]    Crear un nuevo usuario.
        - [X]    Actualizar un usuario existente.
        - [X]    Eliminar un usuario existente.
    - [X]    Debes manejar los casos de error adecuadamente, por ejemplo, si se intenta obtener un usuario que no existe.
    *   Asegúrate de validar los datos de entrada antes de crear o actualizar un usuario:
        - [X]    El nombre debe ser una cadena no vacía.
        - [X]    La edad debe ser un entero positivo.
    - [X]    Agregar pruebas unitarias utilizando la biblioteca pytest.

##  Puntos adicionales (opcional)

Si deseas agregar más desafíos a la prueba técnica, puedes considerar los siguientes puntos:

- [ ]   Agregar paginación a la ruta que obtiene todos los usuarios, permitiendo especificar la cantidad de usuarios a devolver y el número de página.
- [ ]   Implementar autenticación y autorización utilizando tokens de acceso (puedes utilizar bibliotecas como PyJWT).
- [X]   Incluir un Dockerfile que permita la construcción de la API en un contendor. En caso de realizar esta tarea se ha de validar que el contenedor se genera correctamente y se puede ejecutar la API.    

##  Instrucciones

    *   Crea un proyecto de Python utilizando el entorno y las herramientas que prefieras.
    *   Usa una arquitectura orientada a dominio para la estructuración del proyecto (Domain Driven Development)
    *   Usa la codificación guiada por pruebas (TDD)
    *   Implementa la API utilizando FastAPI y asegúrate de cumplir con los requisitos mencionados anteriormente.
    *   Prueba tu API utilizando herramientas como curl, Postman o httpie para asegurarte de que todas las operaciones funcionen correctamente.
    *   Si lo deseas, puedes incluir una breve documentación en forma de comentarios o un archivo README.md explicando cómo usar tu API.
    *   Crea un entorno virtual para la API que nos permita instalar los requirements necesarios para el correcto funcionamiento

# FastAPI
# FastAPI
