
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
import pickle


model = pickle.load(open("trained_model.pkl", "rb"))
classes = ['T-shirt', 'Trouser', 'Pullover', 'Dress','Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

##########################################################################
## Routes
##########################################################################

@app.route("/classify", methods=["POST"])
def classify():

    # Get the data from the request
    data = request.get_json()

    # Convert the data to a numpy array
    pixels = np.array(data["pixels"])

    # Reshape the array to match the model's input shape
    pixels = pixels.reshape(1, -1)

    # Use the model to make a prediction
    prediction = model.predict(pixels)[0]

    # Get the index of the class with the highest prediction
    class_index = np.argmax(prediction)

    # Return the predicted class as a response
    return {"class": classes[class_index]}
    
##########################################################################
## Main
##########################################################################

if __name__ == "__main__":
    app.run(debug=True)