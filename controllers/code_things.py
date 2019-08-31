from flask import Blueprint
from models.code_thing import CodeThing, CodeThingSchema

api = Blueprint('code_things', __name__)
code_thing_schema = CodeThingSchema()

@api.route('/codethings', methods=['GET'])
def index():
    code_things = CodeThing.query.all()
    return code_thing_schema.jsonify(code_things, many=True), 200
