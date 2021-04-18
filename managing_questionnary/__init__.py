from flask import Flask,jsonify
from flask_restful import Api
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint



app_managing_questionnary = Flask(__name__)
api_managing_questionnary = Api(app_managing_questionnary)


from managing_questionnary import config
from managing_questionnary import routes
from managing_questionnary.mongo import init_mongo

if config.env== 'DEVELOPMENT':
    conf = config.DevelopmentConf
else:
    conf = config.ProductionConf

app_managing_questionnary.config.from_object(conf)
init_mongo(app_managing_questionnary)



@app_managing_questionnary.route("/swagger")
def swaggerController():
    swag= swagger(app_managing_questionnary)
    swag['info']['version'] = config.APP_VERSION
    swag['info']['title'] = config.API_NAME
    return jsonify(swag)

swagui_blueprint = get_swaggerui_blueprint(
    conf.SWAGGER_URL,
    conf.DATA_SWAGGER,
    config = {'app_name':'Managing Questionnaries'
    },
)
app_managing_questionnary.register_blueprint(swagui_blueprint, url_prefix=conf.SWAGGER_URL)
