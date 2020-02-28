import json
import falcon
import pickle
from sklearn.linear_model import LogisticRegression


class Predict(object):
    def on_post(self, req, resp):
        raw_body = req.bounded_stream.read()
        body_data = json.loads(raw_body, encoding='utf-8')

        pregnancies = body_data.get('pregnancies')
        glucose = body_data.get('glucose')
        blood_pressure = body_data.get('blood_pressure')
        skin_thickness = body_data.get('skin_thickness')
        insulin = body_data.get('insulin')
        bmi = body_data.get('bmi')
        diabetes_pedigree_function = body_data.get('diabetes_pedigree_function')
        age = body_data.get('age')

        loaded_model = pickle.load(open('finalized_model.pkl', 'rb'))

        result = int(loaded_model.predict([[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree_function,
            age
        ]])[0])

        resp.media = {"outcome": result}
        resp.status = falcon.HTTP_200
