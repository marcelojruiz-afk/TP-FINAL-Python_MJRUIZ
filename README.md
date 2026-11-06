# TP-FINAL-Python_MJRUIZ
Trabajo Final para aprobar  curso de Python


Este es mi trabajo final del curso de Programación con Python C3

AUTOR:Marcelo José Ruiz

El TP FINAL tiene 3 ejercicios, y los ejercicios tratan sobre una supuesta empresa llamada: EcoTech Solutions.

Cada ejercicio está en su propia carpeta.

INSTALACIONES QUE REALICE PARA QUE PUEDA CORRER:

 - Python
 - Django
 - pytest 


Ejercicio 1 – LOS SENSORES

Acá limpio los datos que mandan unos sensores (venían con espacios, con la "C" pegada a la temperatura y a veces sin ubicación).
Después armo un resumen con los sensores que pasan el límite y el promedio de temperatura.

Para probarlo:    python ejercicio_1_sensores/sensores.py



Ejercicio 2 – LOS PRODUCTOS

Hice una clase para los productos y otra para los paneles solares, que hereda de la primera.
El stock está protegido: si alguien quiere poner un número negativo, salta un error (`StockInvalidoError`).
Al final los productos que están bien se guardan en un archivo llamado:  catalogo_ecotech.json

Para probarlo (hay que entrar a la carpeta para que el JSON se guarde ahí):

cd ejercicio_2_productos

python productos.py
cd..



Ejercicio 3 – TEST y LA PAGINA WEB

Primero hice pruebas para ver que el cálculo de emisiones de carbono funcione bien (y que se queje,  si el consumo es negativo).
Después lo usé en una página hecha con Django que muestra el total de emisiones y qué planta consumió más.

Para correr las pruebas:

cd ejercicio_3_auditoria_web/ecotech_web

python -m pytest


Para ver la página:

python manage.py runserver