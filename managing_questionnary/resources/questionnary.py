from flask import request
from flask_restful import Resource, reqparse, abort
from managing_questionnary.modeles import Questionnary
from managing_questionnary.utils.util import response, loginOK, jwt_auth





class QuestionnariesResource(Resource):

    @loginOK
    @jwt_auth
    def get(self, usr):
        '''
        Return all the questionnaries owned by the user
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the elements
            404:
                NO OK, Erreur
        '''
        try:
            liste = list(map(lambda questionnary: questionnary.jsoned(), Questionnary.objects(usr=usr)))
            return response(200, 'Succes', liste)

        except Exception as error1:
            raise(error1)



    @loginOK
    @jwt_auth
    def put(self, usr):
        '''
        Add a questionnary to the user
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the elements
            404:
                NO OK, Erreur
        '''
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('title', type=str, required=True, help="Missing questionnary")
        args = body_parser.parse_args(strict=False) 

        try:

            if 'questionsList' in args:
                questionnary = Questionnary(usr=usr, title=args['title'], questionsList=args['questions_list'], nbrQuestions=len(args["questions_list"])).save()

            else :
                questionnary = Questionnary(usr=usr, title=args['title'], questionsList=[], nbrQuestions=0).save()

            return response(200, 'Success',{'questionnary' : questionnary.jsoned()})

        except Exception as error2:

            return response(400,str(error2),args)





class QuestionnaryByIdResource(Resource):

    @loginOK
    @jwt_auth
    def get(self, usr, listId: str):
        '''
        Return a specific questionnary owned by the user
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the elements
            404:
                NO OK, Erreur
        '''
        try:
            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                return response(404,'Not Found', {"data": "questionnary id not found"})

            return response(200, 'Success', {'questionnary' : questionnary.jsoned()})

        except Exception as error3:

            return response(400,str(error3),{"listId": listId})



    @loginOk
    @jwt_auth
    def delete(self, usr, listId: str):
        '''
        Delete a specific questionnary owned by the user
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the list
            404:
                NO OK, Erreur
        '''
        try:
            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                return response(404,'Not Found', {"data": "questionnary id not found"})

            for question in questionnary.questionsList:
                question.delete()

            questionnary.delete()
            return report(200, 'Success', {'questionnaryId': listId})

        except Exception as error4:
            return response(400,str(error4),{"listId":listId})



    @loginOK
    @jwt_auth
    def patch(self, usr, listId: str):
        '''
        Update a specific questionnary owned by the user
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the  new list
            404:
                NO OK, Erreur
        '''
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('title', type=str, required=True, help="Missing questionnary")
        args = body_parser.parse_args(strict=False) 

        try:
            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                return response(404,'Not Found', {"data": "questionnary id not found"})

            if 'questionsList' in args:
                questionnary.update(title=args['title'],questionsList=args['questionsList'])

            else:
                questionnary.update(title=args['title'])

            questionnary = Questionnary.objects(id=listId).first()

            return response(200, 'Success', {'questionnary' : questionnary.jsoned()})

        except Exception as error5:

            return response(400,str(error5),args)