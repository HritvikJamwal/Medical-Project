# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:15:24 2020

@author: hritvik
"""



from flask import request, jsonify, Flask, render_template


app = Flask(__name__)
       
@app.route('/')
def home():
	return render_template("home.html")










if __name__ == '__main__':
    app.run()
    
    
    
    
