# CarrosApi
Creación de una API simple utilizando el framework Flask para Python. Esta API soporta las siguientes funcionalidades en las rutas:

- ruta por defecto ('/'):

Muestra un mensaje de bienvenida al usuario

- Ruta funcionalidad almacenamiento (/carros):

Dependiendo del método de la petición se ejecuta una funcionalidad:

- GET: Imprime los registros almacenados en el archivo de texto carros.txt

- POST: Almacena los registros entregados en el cuerpo de la petición. Esta se debe hacer un formato JSON teniendo en cuenta la siguiente plantilla:

{
    "Marca": "Renault",
    "Color": "Azul",
    "Estado": "Usado"
}