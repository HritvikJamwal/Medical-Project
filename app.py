# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:15:24 2020

@author: hritvik
"""

from keras.models import load_model
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import request, jsonify, Flask, render_template


app = Flask(__name__)



   
@app.route("/")
def malaria():
    
    return render_template('home.html', prediction = 'hello')
    
          



if __name__ == '__main__':
    app.run()
