from managing_questionnary.mongo import mongo
from managing_questionnary import config
import jwt
from passlib.hash import sha256_crypt
import hashlib


class Question(mongo.Document):

    usr = db.StringField(required=True)
    question = db.StringField(required=True)
    reponse = db.StringField(required=True)
    delai= db.IntField(required=True)

     def jsoned(self):

         return {
             "id":str(self.id),
             "usr" : self.usr,
             "question":self.question,
             "reponse":self.reponse,
             "delai":self.delai
         }



class Questionnary(mongo.Document):

    usr = db.StringField(required=True)
    title = db.StringField(required=True)
    questionsList = db.ListField(db.ReferenceField('Question'))
    nbrQuestions = db.IntField(require=True)



    def jsoned(self):

        return {

            "id":str(self.id),
            "usr" : self.usr,
            "title":self.title,
            "questionList" :list(map(lambda question: question.asJson(), self.questionsList))


        }



class User(mongo.Document):

    usr = mongo.StringField(required=True)
    pwd = mongo.StringField(required=True)



    def jsoned(self):
        return {

            "id":str(self.id),
            "usr":self.usr,
            "pwd":self.pwd

        }

    

    def encode_token(self, user_id):
        return jwt.encode({"usr":self.usr,"pwd":self.pwd}, 'minecraft', algorithm='HS256')



    def hash_pwd(pwd):
        password = sha256_crypt.encrypt(pwd)
          

    
    def verify_pwd(pwd, verif):
        return sha256_crypt.verify(pwd, verif)



    def decode_token(auth_token):

        try:

            return(jwt.decode(auth_token, 'minecraft', algorithms=['HS256']))
        except jwt.ExpiredSignatureError as error1:
            raise error1
        except jwt.InvalidTokenError as error2:

            raise error2