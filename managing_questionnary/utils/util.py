from flask import request
from managing_todo_list.modeles import User
import jwt
import json
from bson import json_util




def response(status: int, msg: str, data: any):

    return {'status': status,'msg': msg,'data': data}



def parse_json(data):

    return json.loads(json_util.dumps(data))



def jwt_auth(f):

  def wrapper(*args, **kwargs):

    try :

        token= request.headers['Authorization']
        payload= User.decode_token(token)
        usr= payload['usr']
        pwd= payload['pwd']

    except jwt.exceptions.InvalidTokenError:
        return response(401, "Invalidtoken",{})

    except Exception as error1:
        raise(error1)

    

    try:

        user = User.objects(usr=usr,pwd=pwd).first()

        if user is None :
            return response(401, "Invalid token",{})

    except Exception as error2:

        return response(400,str(error2),args)

    return f(*args, username, **kwargs)

  return wrapper



def loginOK(f):

  def wrapper(*args, **kwargs):

    try :

        token = request.headers['Authorization']
        usr = User.decode_token(token)

    except jwt.exceptions.InvalidTokenError:

        return sendJson(403, "Invalid token",token)

    except Exception as error3:

        raise(erro3)
    #print(f'''
    #route : {request.url_rule}
    #username : {usr}
    #body : {request.data}
    #''')

    return f(*args, **kwargs)

  return wrapper



def loginNoOk(f):

  def wrapper(*args, **kwargs):

    #print(f'''
    #route : {request.url_rule}
    #username : None
    #body : {request.data}
    #''')

    return f(*args, **kwargs)

  return wrapper