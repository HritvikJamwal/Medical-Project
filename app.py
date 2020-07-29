#Important Modules
from flask import Flask,render_template, url_for ,flash , redirect
#from forms import RegistrationForm, LoginForm
from sklearn.externals import joblib
from flask import request
import numpy as np
import tensorflow
import os
from flask import send_from_directory
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf

#from this import SQLAlchemy
app=Flask(__name__,template_folder='template')



# RELATED TO THE SQL DATABASE
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
#db=SQLAlchemy(app)

#from model import User,Post

#//////////////////////////////////////////////////////////

dir_path = os.path.dirname(os.path.realpath(__file__))
#UPLOAD_FOLDER = dir_path + '/uploads'
# STATIC_FOLDER = dir_path + '/static'
uploads = 'uploads'
static = 'static'

#graph = tf.get_default_graph()
#with graph.as_default():;








@app.route('/upload11', methods=['POST','GET'])
def upload11_file():

    if request.method == 'GET':
        return render_template('index2.html')
    else:
        file = request.files['image']
        pneumonia_path = os.path.join(uploads, file.filename)
        file.save(pneumonia_path)
        pneumonia_model=load_model("chestxray.h5")
        data = image.load_img(pneumonia_path, target_size=(250, 250, 3))
        data = np.expand_dims(data, axis=0)
        data = data * 1.0 / 255
        predicted = pneumonia_model.predict(data)
        answer = "%0.2f"%(predicted[0][0])
        if(predicted>0.50):
            return render_template('predict1.html', answer = answer, colour = 'red')
        else:
            return render_template('predict1.html', answer = answer, colour = 'green')
        
  

@app.route('/upload', methods=['POST','GET'])
def upload_file():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['image']
        malaria_path = os.path.join(uploads, file.filename)
        file.save(malaria_path)
        malaria_model=load_model("malaria_model.h5")
        data = image.load_img(malaria_path, target_size=(100, 100, 3))
        data = np.expand_dims(data, axis=0)
        data = data * 1.0 / 255
        predicted = malaria_model.predict(data)
        answer = "%0.2f"%(predicted[0][0])
        answer = answer - 1
        if(predicted<0.50):
            return render_template('predict.html', answer = answer, colour = 'red')
        else:
            return render_template('predict.html', answer = answer, colour = 'green')           
        

'''
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
'''








@app.route("/") 

@app.route("/home")
def home():
    return render_template("home.html")
 


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cancer")
def cancer():
    return render_template("cancer.html")


@app.route("/diabetes")
def diabetes():
    #if form.validate_on_submit():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/liver")
def liver():
    #if form.validate_on_submit():
    return render_template("liver.html")

@app.route("/kidney")
def kidney():
    #if form.validate_on_submit():
    return render_template("kidney.html")

@app.route("/Malaria")
def Malaria():
    return render_template("index.html")

@app.route("/Pneumonia")
def Pneumonia():
    return render_template("index2.html")









if __name__ == "__main__":
    app.run()
