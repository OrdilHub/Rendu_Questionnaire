from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'question': fields.String(default='Combien?'),
    'uri': fields.Url('questionEndpoint')
}

class QuestionModel(object):
    def __init__(self,questionId,question,reponse,delai):
        self.questionId=questionId
        self.question=question
        self.reponse=reponse
        self.delai=delai


class ToDo(Resource):
    @marshal_with(resource_fields)
    def get (self, **kwargs):
        return QuestionModel(questionId='question_a_repondre', question='Question par defaut')