from flask_restful import Resource

class QuestionNullResource(Resource):

    def get(self):
        return {'Question_une':'Ceci est un exemple de question:alors?'}

class QuestionNull2Resource(Resource):

    def get(self):
        return {'Question_deux':'Ceci est un autre exemple de question:alors?'}