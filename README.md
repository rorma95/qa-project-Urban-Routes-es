# Pruebas para pedir un taxi en la aplicacion Urban Routes
## _Proyecto final de Sprint No. 8 "Automatización de pruebas de la aplicación web"_

## Tarea:
    Se necesita probar el servicio de Urban Routes, tendras que cubrir todo el proceso de pedir un taxi por medio
    de la aplicacion web. Las pruebas deben cubrir estas acciones:  
    1.- Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
    2.- Seleccionar la tarifa Comfort.
    3.- Rellenar el número de teléfono.
    4.-Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV 
    de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar 
    el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla).
    El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido 
    para agregar una tarjeta.
    5.-Escribir un mensaje para el controlador.
    6.- Pedir una manta y pañuelos.
    7.- Pedir 2 helados.
    8.- Aparece el modal para buscar un taxi.
    9.- Esperar a que aparezca la información del conductor en el modal (opcional). 
    Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los 
    demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más 
    difíciles.
    
## Requisitos
- Escribir varias pruebas para comprobar la funcionalidad de Urban Routes. Escribe tus pruebas en el archivo main.py.
- Define los localizadores y métodos necesarios en la clase UrbanRoutesPage y las pruebas en la clase TestUrbanRoutes.
- Escribe pruebas automatizadas que cubran el proceso completo de pedir un taxi.

## Se necesitaran al menos cuatro archivos en total:
- main.py, 
- data.py,
- README.md. 
- .gitignore. 

## Pasos a seguir, usando pycharm:
- Obtener un servidor para la aplicacion Urban Routes.
- Crear una ruta.
- Pedir un taxi usando el metodo flash.
- Agregar informacion necesaria, como numero telefonico y metodo de pago.
- Agregar elementos deseados a la orden.
- Finalizar el pedido esperando que nos asignen un conductor.

## Contenido de los diferentes archivos
- main.py: Se encuentra el codigo con los metodos y pruebas solicitadas.
- data.py: Se guarda los datos necesarios para ingresar en casos especificos, como el numero telefonico, numero de tarjeta, direcciones, etc.
- README.md: Breve descripción de tu proyecto
- .gitignore: Archivo especial para que no se suban en los repositorios archivos inecesarios o por temas de seguridad se deban de ignorar.

## Flujo de las pruebas realizadas.
-	Configurar la dirección.
- 	Seleccionar la tarifa Comfort.
-   Rellenar el número de teléfono.
- 	Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla).
- 	Escribir un mensaje para el controlador.
-   Pedir una manta y pañuelos.
- 	Pedir 2 helados.
-   Aparece el modal para buscar un taxi.
- 	Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más difíciles.
