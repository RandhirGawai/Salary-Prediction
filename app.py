from flask import Flask, render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict_placement():
    experience=float(request.form.get('experience'))
    cgpa=int(request.form.get('cgpa'))
    age=int(request.form.get('age'))
    Interview_score=int(request.form.get('Interview_score'))


    result=model.predict(np.array([experience,cgpa,age,Interview_score]).reshape(1,4))

    return render_template('index.html',result=result)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)