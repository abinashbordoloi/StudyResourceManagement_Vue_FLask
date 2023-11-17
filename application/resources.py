from flask_restful import Resource, Api, reqparse
from .models import StudyResource, db
api = Api(prefix = '/api')


parser = reqparse.RequestParser()
parser.add_argument('rate', type = int, help = 'Rate to change for this resource')
parser.add_argument('description', type = str, help = 'Topic should be a string')
parser.add_argument('resource_link', type = str, help = "Resource Link should be a String")


class StudyMaterial(Resource):
    def get(self):
        return {"Message":"Hello form api"}
    

    def post(self):
        args = parser.parse_args()
        study_resource = StudyResource(**args)
        db.session.add(study_resource)
        db.session.commit()
        pass

api.add_resource(StudyMaterial,'/study_material')
