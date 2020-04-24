# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:23:43 2020

@author: 100293
"""
##pip install flask

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



app= Flask(__name__)
pl=open('model.pkl', 'rb')
model = pickle.load(pl)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = (prediction[0])
    
    return render_template('index.html', prediction_text= "THE PROFIT OBTAINED BY GIVEN OBESERVATION ${}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
    

