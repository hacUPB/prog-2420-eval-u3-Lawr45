[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Lawrence Barrientos Montoya 
ID:  000311633
---

Lo primero que planteo en el codigo es la creacion de las variables, los diccionarios y las llaves de dichos dicsionarios
Creamos diccionarios y llaves de 3 tipos de carros 
Sedan - Deportivo - Camioneta 
Cada uno de estos tipos de carro va a tener 3 modelos 
mediante los diccionarios usamos el tipo de carro como llave para llegar a los modelos: 

      " modelos = {'Sedan':['Corolla','M3','JETTA'],'Deportivo':['Mustang','Camaro','Ferrari'],'Camioneta':['Ranger','Taho','Hilux']} "

Tambien se creea un diccionario para las caracteristicas especiales de cada tipo de carro
Y caracteristicas generales para los 3 tipos de carros

Cada diccionario viene con una stock, que es lo que nos indica la cantidad del producto que se encuntra disponible 
Para cuando el usuario que este comprando vea cuando se acabo un producto y dejar de comprarlo 


Lo siguiente a realizar es un menu de entrada donde el usuario va a ingresar su nombre y su apellido 
para que el programa le de la bienvenida a la pagina con dicho nombre y apellido 


La siguiente seccion del codigo lo que hace es presentar los 3 tipos de carros disponibles
Mostrando la stock que tiene cada uno
Ejm:

      Se tienen los siguientes carros disponibles:  
      1. Sedan:  3
      2. Deportivo 1 
      3. Camioneta:  2


Lo siguiente sera el programa preguntandole al usuario que seleccione un carro para continuar con la compra 
Para poder seguir con los modelos de dichos carros 
Donde podremos ver el precio de cada modelo 

Se realizo y se el menu de seleccion de carros, donde el usuario dira el numero correspondiente al modelo deseado 
y el programa lo mandara a una seccion que le mostrara los 3 tipos de carros dentro de ese segmento
Donde el usuario tendra que escribir el nombre del modelo del carro a seleccionar 
podiendo apreciar el valor de cada uno 

Lo que hace el programa es usar la key que el usuario seleccione para poder abrir el diccionario que contiene los modelos 
Y cada que se haga una compra se restara 1 al modelo seleccionado 

En caso de no tener lo que el usuario desee se le mostrar el mensaje de:
"Lo sentimos, no hay stock para este tipo de carro."

      if carros[tipo_carro] <= 0:
           print('Lo sentimos, no hay stock para este tipo de carro.')
           return None, None


Lo siguiente es las caracteristicas de los carros, de forma general y especifica 
Primero es pedirle al usuario que vaya seleccionando cada caracteristica general 
La cual contiene cada una un valor que se hira sumando al valor base del carro seleccionado 
cuando se temine de seleccionar las caraccteristicas generales se continua con las especificas 
La cual solo es una pero es la que mas valor tiene

Al seleccionar todas las caracteristicas deseadas se mostrara el valor total del carro sumado con las de los agregados 
Ejm:
El total a pagar por su M3 es: $51500


Ya con eso pasamos a la seccion de Hora de recogida
El programa me pedira que ingrese una hora en formato 24H 
Al ingresar la hora deseada el programa simplemente te dara las gracias y te dira la hora elegida para recoger el carro

Y te preguntara si deseas seguir comprando o deseas salir 

      continuar = input("¿Desea comprar otro carro? (s/n): ").lower()
                  if continuar != 's':
                      break

Si deseas seguir el programa empezara de 0 pero con la stock de los carros iniciales 

            continuar = input("¿Desea comprar otro carro? (s/n): ").lower()
            if continuar != 's':
                break

reducida por la compra que se acaba de realizar 
Asi haciendo que no se puedan comprar infinitamente 
Ni que se agoten al comprar solo un carro 

Ya que el programa verifica si hay carros disponibles y el numero de stock

            if all(stock == 0 for stock in carros.values()):
                print("Todos los carros están agotados.")
                break

