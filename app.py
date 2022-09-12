import pickle
from flask import Flask,request,render_template
from logger import  *


app=Flask(__name__)
model=pickle.load(open('model1.pkl','rb'))

@app.route("/home")
def home():
    return "Welcome to home page"

@app.route("/predict")
def predict():
    return "predicted output will be here"



if __name__=='__main__':
    app.run(debug=True)