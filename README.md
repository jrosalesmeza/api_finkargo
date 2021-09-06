## API | PRUEBA TECNICA

[![N|Solid](https://finkargo.com/static/media/finkago-logo.66dcfc4b.svg)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

El API contiene 7 endpoints y fueron desarrollados en Python bajo el entorno de trabajo Flask.

## Documentación de API
https://documenter.getpostman.com/view/12949914/U16gPSUF

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
pip install -r api_finkargo/src/requirements.txt
```
Configurar variables de entorno.
```sh
set FLASK_APP= src/app.py
set FLASK_ENV=development
```
## Base de datos
Cree la base de datos en el motor de su preferencia y configure las credenciales de acceso de esta en el archivo **app**.
```sh
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/nameBaseDatos'
```
Crear tablas, los siguientes comandos se debe realizar en la carpeta **src**.
```sh
python
>> from app import db
>> db.create_all()
```
Correr la aplicación
```sh
flask run
127.0.0.1:5000
```

## Uso de Libreria

1. Antes de crear un usuario por primera vez, es necesario agregar roles y nacionalidades.
2. Crear usuario Admin.
3. Consumir el resto de endpoints.

## Librerias

Las Librerias que se usaron en la API son:

| Libreria | Detalle |
| ------ | ------ |
| SQLAlchemy | Interacción ORM con las entidades |
| HTTPBasicAuth | Autenticación |

## Autor
Jose Luis Rosales Meza
jrosalesmeza@gmail.com

