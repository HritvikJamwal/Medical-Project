# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:15:24 2020

@author: hritvik
"""


import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import request, jsonify, Flask, render_template


app = Flask(__name__)



model = load_model('malaria_model.h5')  
@app.route("/")
def malaria():
    
    data = image.load_img('normalmalaria.jpeg', target_size=(100, 100, 3))
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255
    predicted = model.predict(data)
    return render_template('home.html')
    
          



if __name__ == '__main__':
    app.run()
