from flask import request
from flask_restful import Resource, reqparse, abort
from app.models import Question, Questionnary
from managing_questionnary.utils.util import response, loginOK, jwt_auth



class QuestionsResource(Resource):

    @loginOK
    @jwt_auth
    def get(self, usr, listId: str):
        '''
        Return all the questions contained in the questionnary of the user
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

            return response(200, 'Success', {'questionnaryId': listId,'questions': questionnary.jsoned()['questionsList']})

        except Exception as error1:
            return response(400,str(error1),{"listId":listId})



    @loginOK
    @jwt_auth
    def put(self, usr, listId: str):
        '''
        Add question to questionnary
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the new list
            404:
                NO OK, Erreur
        '''
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('question', type=str, required=True, help="Missing question")
        body_parser.add_argument('delai', type=int, required=True, help="Missing delai")
        args = body_parser.parse_args(strict=False)

        try:
            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                return response(404,'Not Found', {"data": "questionnary id not found"})

            question = Question(usr=usr, question=args['question'], reponse="",delai = args['delai']).save()
            questionnary.update(pushQuestionnary=question,usr=usr)
            newQuestionnary = Questionnary.objects(id=listId, usr=usr).first()
            return response(200, 'Success', {"question": question.asJson(),"newQuestionnary": newQuestionnary.jsoned()})

        except Exception as error2:

            return response(400,str(error2),{"listId":listId})


class QuestionsByIdResource(Resource):

    @loginOK
    @jwt_auth
    def get(self, usr, listId: str, questionId: str):
        '''
        Get a specific question from questionnary
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the element
            404:
                NO OK, Erreur
        '''
        try:
            question = Question.objects(id=questionId, usr=usr).first()

            if question is None:
                return response(404,'Not Found', {"data": "question id not found"})

            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                
                return response(404,'Not Found', {"data": "questionnary id not found"})

            return response(200, 'Success', {'question': question.jsoned(),'questionnary': questionnary.jsoned()['id']})

        except Exception as error3:
            return response(400,str(error3),{"listId":listId})



    @loginOK
    @jwt_auth
    def delete(self, usr, listId: str, questionId: str):
        '''
        Delete a specific question from questionnary
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the new list
            404:
                NO OK, Erreur
        '''
        try:
            question = Question.objects(id=questionId, usr=usr).first()

            if question is None:
                return response(404,'Not Found', {"data": "question id not found"})

            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                return response(404,'Not Found', {"data": "questionnary id not found"})

            question.delete()
            questionnary.update(pullQuestionnary=questionId,usr=usr)

            return response(200, 'Success', {'questionnary': questionnary,"listId": listId})

        except Exception as error4:

            return response(400,str(error4),{"listId":listId})



    @loginOK
    @jwt_auth
    def patch(self, usr, listId: str, questionId: str):
        '''
        Update a specific TODOfrom TODOS list
        ---
        tags:
            -Flask API
        responses:
            200:
                OK, JSON Format of the new element
            404:
                NO OK, Erreur
        '''
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('question', type=str, required=True, help="Missing question")
        body_parser.add_argument('delai', type=str, required=True, help="Missing delai")
        args = body_parser.parse_args(strict=False) 

        try:

            question = Question.objects(id=toDoId, usr=usr).first()
            if question is None:
                return response(404,'Not Found', {"data": "question id not found"})
            questionnary = Questionnary.objects(id=listId, usr=usr).first()

            if questionnary is None:
                return response(404,'Not Found', {"data": "questionnary id not found"})

            question.update(usr=usr,question=args['question'],delai=args['delai'])
            question= Question.objects(id=questionId, usr=usr).first()
            return response(200, 'Success', {'question' : question.jsoned()})

        except Exception as error5:

            return response(400,str(error5),args)