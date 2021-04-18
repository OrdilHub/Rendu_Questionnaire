from managing_questionnary import api_managing_questionnary
from managing_questionnary.resources.questionnullresource import QuestionNullResource, QuestionNull2Resource


api_managing_questionnary.add_resource(QuestionNullResource,'/','/null')
api_managing_questionnary.add_resource(QuestionNull2Resource,'/null2')
api.add_resource(AuthResource, '/account')
api.add_resource(LoginResource, '/login')
api.add_resource(QuestionnaryResource, '/questionnaries')
api.add_resource(QuestionnaryByIdResource, '/questionnaries/<string:questionnary_id>')
api.add_resource(QuestionResource, '/questionnaries/questions/<string:questionnary_id>')
api.add_resource(QuestionByIdResource, '/questionnaries/questions/<string:list_id>/<string:question_id>')