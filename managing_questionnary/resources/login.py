from flask_restful import Resource, reqparse, abort
from managing_questionnary.modeles import User
from managing_questionnary.utils.util import response, loginNoOk





class LoginResource(Resource):



    @loginNoOk

    def post(self):

        body_parser = reqparse.RequestParser()
        body_parser.add_argument('usr', type=str, required=True, help="Missing loging")
        body_parser.add_argument('pwd', type=str, required=True, help="Missing password")
        args = body_parser.parse_args(strict=True) 



        try:

            user = User.objects(usr=args['usr']).first()

            if user is None :
                return response(404,"IncorrectPassword or Username", {'usr' : args['usr']})


            if not User.verify_pwd(args['pwd'], user.pwdd):
                return sendJson(404,"IncorrectPassword or Username", {'usr' : args['usr']})

            else:
                token= user.encode_token(user.id)
                return response(200, "Success", {'user': user.jsoned(),'token': token})

        except Exception as err:
            return response(400,str(err),args)