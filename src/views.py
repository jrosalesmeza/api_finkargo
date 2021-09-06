from flask import request
from flask import json
from flask.json import jsonify
from app import app,auth,db
from models import *



@auth.verify_password #Se marca con el decorador "verify_password", el cual nos verifica si el usuario y el Password enviados son correctos y se pueda consumir las APIs
def verify_password(username, password):
    user=User.query.filter(User.email==username).first()
    if user is not None and user.check_password(password):
        return username


@app.route('/clasificar_numeros', methods=['POST'])
@auth.login_required # Se marca con el decorador "Login_Required" con el fin de que se debe autenticar primero para poder consumir esta API.
def endpoint1(): # Primer Punto
    data= request.json
    respuestaFinal ={}
    if data is not None: #Verificamos si existe información
        status=200
        if "sin clasificar" in data and all(type(i) == int for i in data['sin clasificar']): #Verificamos si el JSON enviado existe la "Propiedad" sin Clasificar, además verificamos si todos los objetos enviados son numeros enteros
            array= data['sin clasificar']
            numbers_clasificados=clasficarNumeros(array) # Pasamos el arreglo y usamos la función clasificar.
            respuestaFinal['sin clasificar']=array #Se agrega al diccionario "Respuesta Final" en la llave "sin clasificar" la información enviada por el usuario.
            respuestaFinal['clasificado']=numbers_clasificados#Se agrega al diccionario "Respuesta Final" en la llave "clasificado" la información clasificada.
        else:
            respuestaFinal['error']="INFORMACIÓN INVALIDA" 
            status=400
    else:
            respuestaFinal['error']="ENVIAR INFORMACIÓN"
            status=400
        
    return jsonify(respuestaFinal), status # Se retorna en JSON el diccionario "Respuesta Final"


def clasficarNumeros(numbers):
    repetidos=[]
    sinRepetir =[]

    for number in numbers:
        if number not in sinRepetir:
            sinRepetir.append(number)
        else:
            repetidos.append(number)
    
    ordenados=list(sorted(sinRepetir))

    ordenados.extend(repetidos)

    return ordenados


@app.route('/balance_mensual',methods=['POST'])
@auth.login_required
def endpoint2(): # Punto Numero 2
    data= request.json
    respuestaFinal ={}
    status=200
    if data is not None:
        if "Mes" in data and "Ventas" in data and "Gastos" in data: # Se verifica si en el JSON enviado, existe las propiedades "Ventas", "Gastos", "Mes"

            if len(data['Mes']) == len(data['Ventas'])== len(data['Gastos']): #Se verifica si la información enviada contiene la misma cantidad de información en cada arreglo
                if all(type(i) == int or type(i)==float for i in data['Ventas']) and all(type(i) == int or type(i)==float for i in data['Gastos']):# Se verifica si los valores enviados en Ventas y Gastos corresponden a numero entero o flotante.
                    informacion=[]
                    for i in range(len(data["Mes"])): #Se crea un ciclo el cual inicia en 0 hasta la longitud de uno de los arreglos enviados.
                        informacion.append(Balance(data['Mes'][i],data['Ventas'][i],data['Gastos'][i])) # Se agrega al arreglo "informacion" una instancia en base a la clase Balance, el cual contiene las propiedades mes, ventas, gastos y balance, esta ultima se calcula internamente en el constructor del objeto.                       
                    respuestaFinal=json.dumps([z.__dict__ for z in informacion]) # Se recorre y se convierte cada instancia del arreglo "informacion" a un diccionario (Esto con el fin de poder "Serializar el objeto") 
                else:
                    status=400
                    respuestaFinal['error']='Alguno de los valores ingresados en VENTAS o GASTOS no corresponden a un formato numérico'
                    
            else:
                respuestaFinal['error']="Información Incorrecta"
                
        else:
            status=400
            respuestaFinal['error']="Información Incorrecta"
        
    return respuestaFinal,status

class Balance():
    Mes=''
    Gastos=0
    Ventas=0
    Balance=0
    def __init__(self,mes,ventas,gastos):
        self.Mes=mes
        self.Ventas=ventas
        self.Gastos=gastos
        self.Balance=ventas-gastos


#Agregar, Modificar, Listar
@app.route('/add_roles', methods=['POST'])
def add_roles():
    data= request.json
    print(data)
    try:
        for obj in data:
            db.session.add(Rol(obj))
        db.session.commit()
        return "Roles agregados con éxito",200
    except:
        return "Roles Repetidos",200
    

@app.route('/add_nationalities', methods=['POST'])
def add_nationalities():
    data= request.json
    if data is not None:
        try:
            for obj in data:
                temp=Nationality(**obj)
                db.session.add(temp)
            db.session.commit()
            return "Nacionalidades agregadas con éxito",200
        except:
            return "Nacionalidades Repetidas",400

    return '',200


@app.route('/add_user', methods=['POST'])
# @auth.login_required
def add_user():
    data= request.json
    if (data is not None and "name" in data and "email" in data and "password" in data
    and "nationality_id" in data and type(data['password'])==str and "rol_id" in data):
        if User.query.filter(User.email==data['email']).first() is None:
            user=User(**data)
            try:
                db.session.add(user)
                db.session.commit()
                return jsonify("Usuario creado con éxito id_user= {}".format(user.id)),200
            except Exception as ex:
                return jsonify({"error":str(ex)}),500
        else:
            return jsonify({"error":"El email {} ya esta registrado".format(data['email'])}),400
    else:
        return jsonify('Información Invalida'),400


@app.route('/users')
@auth.login_required
def list_users():
    return jsonify(Users=[user.serialize for user in User.query.all()])

@app.route('/users/<string:id_user>')
@auth.login_required
def get_user(id_user):
    userFind=User.query.get(id_user)
    if userFind is not None:
        return jsonify(userFind.serialize),200
    else:
        return jsonify({"msj":"No existe el usuario"})



@app.route('/edit_user/<string:id_user>', methods=['PUT'])
@auth.login_required
def edit_user(id_user):
    data= request.json
    userFind=User.query.get(id_user)
    if userFind is not None:
        if ("nationality_id" in data and "rol_id" in data):
            userFind.nationality_id=data["nationality_id"]
            userFind.rol_id=data["rol_id"]
            db.session.commit()
            return jsonify(userFind.serialize),200
        else:
            return jsonify('Información Invalida'),400
    else:
        return jsonify({"msj":"No existe el usuario"})

@app.route('/delete_user/<string:id_user>', methods=['DELETE'])
@auth.login_required
def delete_user(id_user):
    userFind=User.query.get(id_user)
    if userFind is not None:
        db.session.delete(userFind)
        db.session.commit()
        return jsonify("Usuario eliminado"),200
    else:
        return jsonify({"msj":"No existe el usuario"})


