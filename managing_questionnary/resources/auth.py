from flask import request
from flask_restful import Resource,reqparse,abort
from managing_questionnary.modeles import User
from managing_questionnary.utils.util import response, loginNoOk



class AuthResource(Resource):

    def post(self):

        body_parser = reqparse.RequestParser()
        body_parser.add_argument('usr', type=str, required=True, help="Missing login")
        body_parser.add_argument('pwd', type=str, required=True, help="Missing pssword")
        args = body_parser.parse_args(strict=True) 

        try:       
            user = User(usr=args['usr'],pwd=User.hash_pwd(args['pwd'])).save()
            return response(200, "Success", {'user' : user.jsoned()})

        except Exception as err:
            return response(400,str(err),args)

