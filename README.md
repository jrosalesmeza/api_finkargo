## API | PRUEBA TECNICA

[![N|Solid](https://finkargo.com/static/media/finkago-logo.66dcfc4b.svg)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

El API contiene 7 endpoints y fueron desarrollados en Python bajo el entorno de trabajo Flask.

## Funcionalidades

- Autenticación de usarios (Basic Auth)
- Lista, agrega, elimina y edita usuarios.
- Permite agregar roles y nacionalidades.
- Ordena una lista determinada de numeros enteros.
- Retorna el balance mensual dado un diccionario de datos.


## Inicio e instalación
Requiere de Python para correr.

Se crea y se activa entorno virtual y se instalan librerias que se encuentran en "requirements.txt"
```sh
cd api_finkargo
python -m venv env
cd api_finkargo/env/scripts
activate
pip install -r requirements.txt
```
Configurar variables de entorno.
```sh
set FLASK_APP= src/app.py
set FLASK_ENV=development
```
Crear base de datos, los siguientes comandos se debe realizar en la carpeta src.
```sh
python
>> import app from db
>> db.create_all()
```
Correr la aplicación
```sh
flask run
127.0.0.1:5000
```

## URL API
https://documenter.getpostman.com/view/12949914/U16gPSUF

## Uso de Libreria

- Agregar roles y nacionalidades.
- Crear usuario Admin.
- Consumir el resto de endpoints.

## Librerias

Las Librerias que se usaron en la API son:

| Libreria | Detalle |
| ------ | ------ |
| SQLAlchemy | Interacción ORM con las entidades |
| HTTPBasicAuth | Autenticación |

## Autor
Jose Luis Rosales Meza
jrosalesmeza@gmail.com