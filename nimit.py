from flask import Flask,Response,render_template
from flask import request
import pandas as pd
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

@app.route('/uploader', methods = ['GET','POST'])
def upload_file():
    try:
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print('file uploaded successfully')
        return 'file uploaded successfully'
    except Exception as e:
        print(e)

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        column_data = pd.read_csv(path + '/data/columns.csv')
        column_1 = (column_data.columns[0])
        print("column 1",column_1)
        column_2 = (column_data.columns[1])
        column_3 = (column_data.columns[2])
        column_4 = (column_data.columns[3])
        column_5 = (column_data.columns[4])
        
        linReg1 = pickle.load(open('predict1.pkl', 'rb'))
        linReg2 = pickle.load(open('predict2.pkl', 'rb'))
        linReg3 = pickle.load(open('predict3.pkl', 'rb'))
        linReg4 = pickle.load(open('predict4.pkl', 'rb'))
        linReg5 = pickle.load(open('predict5.pkl', 'rb'))
        column_data = pd.read_csv(path+'/data/columns.csv')

        req_body = request.get_json(force=True)
        print(req_body)

        # For value 1 ,Price
        if req_body[column_1] == '':
            param1 = req_body[column_2]
            param2 = req_body[column_3]
            param3 = req_body[column_4]
            param4 = req_body[column_5]
            pred = linReg1.predict([[param1, param2, param3, param4]])
            result = pred[0]
            msg = {
                "Predicted Price is": "%s" % (result)
            }
            resp = Response(response=json.dumps(msg),
                            status=200,
                            mimetype="application/json")
            return resp
        # For value 2, Bedrooms
        if req_body[column_2] == '':
            param1 = req_body[column_3]
            param2 = req_body[column_4]
            param3 = req_body[column_5]
            param4 = req_body[column_1]
            pred = linReg2.predict([[param1, param2, param3, param4]])
            result = pred
            msg = {
                "Predicted Bedrooms are": "%s" % (result)
            }
            resp = Response(response=json.dumps(msg),
                            status=200,
                            mimetype="application/json")
            return resp
        # For value 3, Size
        if req_body[column_3] == '':
            param1 = req_body[column_2]
            param2 = req_body[column_4]
            param3 = req_body[column_5]
            param4 = req_body[column_1]
            pred = linReg3.predict([[param1, param2, param3, param4]])
            result = pred
            msg = {
                "Predicted size is": "%s" % (result)
            }
            resp = Response(response=json.dumps(msg),
                            status=200,
                            mimetype="application/json")
            return resp
        # For value 4, Age
        if req_body[column_4] == '':
            param1 = req_body[column_3]
            param2 = req_body[column_2]
            param3 = req_body[column_5]
            param4 = req_body[column_1]
            pred = linReg4.predict([[param1, param2, param3, param4]])
            result = pred
            msg = {
                "Predicted Age ": " is %s" % (result)
            }
            resp = Response(response=json.dumps(msg),
                            status=200,
                            mimetype="application/json")
            return resp
        # For value 5, Bathrooms
        if req_body[column_5] == '':
            param1 = req_body[column_3]
            param2 = req_body[column_2]
            param3 = req_body[column_4]
            param4 = req_body[column_1]
            pred = linReg5.predict([[param1, param2, param3, param4]])
            result = pred
            msg = {
                "Predicted Bathrooms are": "%s" % (result)
            }
            resp = Response(response=json.dumps(msg),
                            status=200,
                            mimetype="application/json")
            return resp
    except Exception as e:
        print(e)
if __name__ == '__main__':
    app.run(debug=True,port=port)