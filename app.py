# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:15:24 2020

@author: hritvik
"""



import numpy


import numpy as np
from keras.models import load_model


from flask import request, jsonify, Flask, render_template
import base64
import io
from PIL import Image



app = Flask(__name__)
       
@app.route('/')
def home():
	return render_template('home.html')










if __name__ == '__main__':
    app.run()
    
    
    
    
