from flask import Flask
from flask import request,Response
import os
import json
import pandas as pd
path = os.getcwd()
app = Flask(__name__)
column_data = pd.read_csv(path + '/data/columns.csv')
column_1 = (column_data.columns[0])
column_2 = (column_data.columns[1])
column_3 = (column_data.columns[2])
column_4 = (column_data.columns[3])
column_5 = (column_data.columns[4])

print("column 1",column_1)
print("column 2",column_2)
print("column 3",column_3)
print("column 4",column_4)
print("column 5",column_5)

@app.route('/testthe', methods=['POST'])
def justtest():
    try:
        req_body = request.get_json(force=True)
        print("before param")
        print("req_body",req_body)
        print("column_1",column_1)

        #param1 = req_body['Size']
        param1 = req_body[column_2]
        print("after param")
        print("value",param1)
        result = param1
        # for i in req_body:
        # key[i]
        msg = {
            "Predicted size is": "%s" % (result)
        }
        resp = Response(response=json.dumps(msg),
                        status=200,
                        mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
if __name__ == '__main__':
    app.run(debug=True,port=3000)