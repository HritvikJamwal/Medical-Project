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



model = load_model('malaria_model.h5')
    
def malaria():
    data = image.load_img('infectedmalaria.jpeg', target_size=(100, 100, 3))
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255
    predicted = model.predict(data)
    print("Chances of infected cell:", (("%0.2f"%(1-predicted))))
    
          
malaria()
