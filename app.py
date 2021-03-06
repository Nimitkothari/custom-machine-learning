from flask import Flask,Response,render_template
from flask import request
from werkzeug.utils import secure_filename
import json
import pickle
import os
path = os.getcwd()
#template_path=path+'/templates'
port = int(os.getenv("PORT", 3000))
upload_folder = path
ALLOWED_EXTENSIONS = set(['pkl','txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/upload')
def upload():
   return render_template('upload.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # For Size
        linReg3 = pickle.load(open('predictSize.pkl', 'rb'))
        req_body = request.get_json(force=True)
        if req_body['Size'] == '':
            param1 = req_body['Bedrooms']
            param2 = req_body['Age']
            param3 = req_body['Bathrooms']
            param4 = req_body['Price']
            pred = linReg3.predict([[param1, param2, param3, param4]])
            result = pred[0]
            msg = {
                "Predicted size is": "%s" % (result)
            }
            resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictPrice', methods=['POST'])
def predict_price():
    try:
        # For Price
        linReg1 = pickle.load(open('predictPrice.pkl', 'rb'))
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Bedrooms']
        param3 = req_body['Age']
        param4 = req_body['Bathrooms']
        pred = linReg1.predict([[param1, param2, param3, param4]])
        result = pred[0]
        msg = {
                "Predicted Price is": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictBedrooms', methods=['POST'])
def predict_bedrooms():
    try:
        # For Bedrooms
        linReg2 = pickle.load(open('predictBedrooms.pkl', 'rb'))
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Age']
        param3 = req_body['Bathrooms']
        param4 = req_body['Price']
        pred = linReg2.predict([[param1, param2, param3, param4]])
        result = pred[0]
        msg = {
                "Predicted Bedrooms are": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictAge', methods=['POST'])
def predict_age():
    try:
        # For Age
        linReg4 = pickle.load(open('predictAge.pkl', 'rb'))
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Bedrooms']
        param3 = req_body['Bathrooms']
        param4 = req_body['Price']
        pred = linReg4.predict([[param1, param2, param3, param4]])
        result = pred[0]
        msg = {
                "Predicted Age ": " is %s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictBathrooms', methods=['POST'])
def predict_bathrooms():
    try:
        # For Bathrooms
        linReg5 = pickle.load(open('predictBathrooms.pkl', 'rb'))
        print('after model loaded')
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Bedrooms']
        param3 = req_body['Age']
        param4 = req_body['Price']
        pred = linReg5.predict([[param1, param2, param3, param4]])
        result = pred[0]
        msg = {
                "Predicted Bathrooms are": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)

@app.route('/uploader', methods = ['GET','POST'])
def upload_file():
    try:
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print('file uploaded successfully')
        return 'file uploaded successfully'
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)