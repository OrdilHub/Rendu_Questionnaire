env = 'DEVELOPMENT'
#PRODUCTION_SERVER=
API_NAME='Managing Questionnary'
APP_VERSION='1.0'

class BaseConf():
    DEBUG =True

class DevelopmentConf(BaseConf):
    SWAGGER_URL ='/api/docs'
    DATA_SWAGGER = 'http://localhost:5000/swagger'

# class ProductionConf(BaseConf):
#     DEBUG= False
#     SWAGGER_URL='/api/docs'
#     DATA_SWAGGER='http://'+ PRODUCTION_SERVER +':5000/swagger' 