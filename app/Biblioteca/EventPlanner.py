# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json, g

EventPlanner = Blueprint('EventPlanner', __name__)


@EventPlanner.route('/eventplanner/ACancelReservation')
def ACancelReservation():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VShowEvent', 'msg':[ur'Reservación exitosamente cancelada']}, {'label':'/VShowEvent', 'msg':[ur'Error al cancelar reservación']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@EventPlanner.route('/eventplanner/ACreateEvent', methods=['POST'])
def ACreateEvent():
    #Access to POST/PUT fields using request.form['name']
    #Access to file fields using request.files['name']
    results = [{'label':'/VShowEvent', 'msg':[ur'Evento creado exitosamente']}, {'label':'/VRegisterEvent', 'msg':[ur'Error al crear evento']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


from app.model.user import User 

@EventPlanner.route('/eventplanner/ACreateUser', methods=['POST'])
def ACreateUser():
    #POST/PUT parameters
    params = request.get_json()



    results = [ {'label':'/VLoginUser', 'msg':[ur'Usuario registrado exitosamente']}, 
                {'label':'/VRegisterUser', 'msg':[ur'Error al crear usuario']}, ]


    user = User(params['data'])
    if user.save():
        res = results[0]
    else:
        res = results[1]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/ADeleteEvent')
def ADeleteEvent():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VListEvents', 'msg':[ur'Evento eliminado exitosamente']}, {'label':'/VListEvents', 'msg':[ur'Error al eliminar evento']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/ADeleteUser')
def ADeleteUser():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VListUsers', 'msg':[ur'Usuario eliminado exitosamente']}, {'label':'/VListUsers', 'msg':[ur'Error al eliminar usuario']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AEditEvent', methods=['POST'])
def AEditEvent():
    #Access to POST/PUT fields using request.form['name']
    #Access to file fields using request.files['name']
    results = [{'label':'/VShowEvent', 'msg':[ur'El evento ha sido actualizado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AEvents')
def AEvents():
    #GET parameter
    requestedEvent = request.args['requestedEvent']
    results = [{'label':'/VListEvents', 'msg':[ur'Se listan los eventos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AGenerateCertificate')
def AGenerateCertificate():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCertificate', 'msg':[ur'Certificado exitosamente generado']}, {'label':'/VShowEvent', 'msg':[ur'Error al generar certificado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AGenerateCredentials')
def AGenerateCredentials():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCredential', 'msg':[ur'Credenciales exitosamente generadas']}, {'label':'/VShowEvent', 'msg':[ur'Error al generar credenciales']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/ALogOutUser')
def ALogOutUser():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VLoginUser', 'msg':[ur'Sesión exitosamente cerrada'], "actor":None}, {'label':'/VHome', 'msg':[ur'Error al cerrar sesión']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/ALoginUser', methods=['POST'])
def ALoginUser():
    #POST/PUT parameters
    params = request.get_json()

    user = User(params)

    results = [ {'label':'/VHome', 'msg':[], "actor":user.user }, 
                {'label':'/VLoginUser', 'msg':[ur'Error al iniciar sesión']}, ]



    if user.authenticate():
        res = results[0]
    else:
        res = results[1]


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AReserveEvent')
def AReserveEvent():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VShowEvent', 'msg':[ur'Evento reservado exitosamente']}, {'label':'/VShowEvent', 'msg':[ur'Error al reservar evento']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AUsers')
def AUsers():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VListUsers', 'msg':[ur'Se listan los usuarios']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/AVerifyAssitance')
def AVerifyAssitance():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VListUsers', 'msg':[ur'Asistencia verificada']}, {'label':'/VListUsers', 'msg':[ur'Error al verificar asistencia']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VCertificate')
def VCertificate():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VCredential')
def VCredential():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VEditEvent')
def VEditEvent():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VHome')
def VHome():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VListEvents')
def VListEvents():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VListUsers')
def VListUsers():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VLoginUser')
def VLoginUser():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VRegisterEvent')
def VRegisterEvent():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VRegisterUser')
def VRegisterUser():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@EventPlanner.route('/eventplanner/VShowEvent')
def VShowEvent():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
