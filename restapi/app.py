from typing import List
from flask import Flask
from flask_restful import Resource, Api, reqparse
import joblib
import os
import numpy as np
from pathlib import Path


model_path = Path(__file__).parent.parent.joinpath(os.environ.get("MODEL_PATH"))
model = joblib.load(model_path)

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('insulation_tickness', type=list, required=True, location='json')
parser.add_argument('u_values', type=list, required=True, location='json')


class EnergyUse(Resource):
    def get(self):
        args = parser.parse_args()
        predictions = model.predict(np.array([args['insulation_tickness'], args['u_values']]).T)

        return {"predictions": list(predictions)}
        
    
api.add_resource(EnergyUse, '/annual_energy_use')


if __name__ == '__main__':
    app.run(debug=True)
