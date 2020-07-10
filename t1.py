from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from flask_cors import CORS, cross_origin
from json import dumps
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pickle

import pandas as pd
df=pd.read_csv('maindata.csv')

df=df.dropna()


le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
  
df['State_Name']= le1.fit_transform(df['State_Name']) 
df['District_Name']= le2.fit_transform(df['District_Name'])
df['Season']= le3.fit_transform(df['Season'])
df['Crop']= le4.fit_transform(df['Crop'])

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    test = pd.read_csv("test.csv")
    print(test) 
    print("KKKK")

@app.route("/employee",methods=['POST'])
def hello1(): 
    b = request.get_json()
    test = pd.io.json.json_normalize(b)
    print(test)
    test['State_Name']= le1.transform(test['State_Name']) 
    test['District_Name']= le2.transform(test['District_Name'])
    test['Crop']= le4.transform(test['Crop'])
    test['Season']= le3.transform(test['Season'])
    n = test.rename_axis('ID').values
    n = n.astype(int)
    prediction = model.predict(n)
    df1 = pd.DataFrame(prediction )
    df1 = df1.to_json()
    print(df1)
    
    return df1

class Employees(Resource):
    def get(self):
        return 129 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return employee_id 

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

if __name__ == '__main__':
     app.run(port=5000)