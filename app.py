import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

import zipfile
import pickle

# Path to the zip file
zip_path = "classifier.zip"

# Open the zip file and extract the .pkl content
with zipfile.ZipFile(zip_path, 'r') as z:
    # List files inside the zip (if needed)
    
    # Open the .pkl file from the zip
    with z.open('classifier.pkl') as f:
        model = pickle.load(f)








# Create flask app
flask_app = Flask(__name__)
#model = pickle.load(open("C:/Users/LENOVO/Desktop/MLAPP/classifier.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("testing.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
        
        float_features =[int(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        message=" "
        if ('Theft1' in prediction[0]):
             message="Involves a considerable reduction in electricity consumption during the day, calculated by multiplying the consumption by a randomly chosen value between 0.1 and 0.8."
        elif 'Theft2' in prediction:
             message="Electricity consumption drops to zero at random and during an arbitrary period."
        elif 'Theft3' in prediction:
             message="Similar to Theft Type 1, but each consumption value (each hour) is multiplied by a random number."
        elif 'Theft4' in prediction:
             message="A random fraction of the mean consumption is generated for each hour."
        elif 'Theft5' in prediction :
             message="Reports the mean consumption for each hour."
        else:
             message="Error in prediction"
        return render_template("result.html",messages=message, prediction_text =prediction[0])

if __name__ == "__main__":
    flask_app.run(debug=True)