from flask import Flask, request, jsonify, abort
from models import db
from models import users_has_cultivos, cultivos, cultivos_has_biodispositivos
from format_helpers import fill_response
import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD= os.environ.get('DB_PASSWORD')

conn = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@biobottest.ccttyurgugvu.us-east-1.rds.amazonaws.com:3306/biobot_first_release"
app = Flask(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETSUPERKEY'
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)




#Single Endpoint

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/cultivos", methods=['GET', 'POST'])
def cultivos():
    if request.method == 'GET':
        page = request.args.get('page',1,type=int)
        per_page = request.args.get('per_page', 1, type=int)
        user_id = int(request.args['user_id'])
        user_cultivos = users_has_cultivos.query.filter_by(users_id=user_id).paginate(page=page, per_page=per_page)

        if user_cultivos:
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
        else:
            response = {
                "data" : "User does not have cultivos"
            }
        return jsonify(response)
    else:
        return "Method not allowed", 405






if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)