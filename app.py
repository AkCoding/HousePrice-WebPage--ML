#Import Libraries
from flask import Flask, request, render_template


import model # load model.py

app = Flask(__name__)

# render htmp page
@app.route('/')
def home():
    return render_template('index.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
    form = model.InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = "Yes ! You are eligible"
    else:
        result = "You are not eligible"  
    return render_template('index.html', prediction_text='{}'.format(result))
if __name__ == "__main__":
    app.run()
