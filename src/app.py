from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import users_has_cultivos, cultivos, cultivos_has_biodispositivos
from format_helpers import fill_response
import os

USERNAME = os.environ.get('API_USERNAME')
PASSWORD = os.environ.get('API_PASSWORD')


#conn = "mysql+pymysql://:shinyWhal322@biobottest.ccttyurgugvu.us-east-1.rds.amazonaws.com:3306/biobot_first_release"
db_connection = f"mysql+pymysql://:{PASSWORD}@{USERNAME}.ccttyurgugvu.us-east-1.rds.amazonaws.com:3306/biobot_first_release"
app = Flask(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETSUPERKEY'
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
db.init_app(app)




#Single Endpoint
@app.route("/cultivos/", methods=['GET'])
def cultivos():
    page = request.args.get('page',1,type=int)
    per_page = request.args.get('per_page', 1, type=int)
    user_id = int(request.args['user_id'])
    user_cultivos = users_has_cultivos.query.filter_by(users_id=user_id).paginate(page=page, per_page=per_page)

    response = {
        "data": fill_response(user_cultivos),
        "meta": {
            "page": user_cultivos.page,
            "pages" : user_cultivos.pages,
            "total_count" : user_cultivos.total,
            "next_page" : user_cultivos.next_num,
            "has_next" : user_cultivos.has_next,
            "has_prev" : user_cultivos.has_prev,
        }
    }


    return jsonify(response)






if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')