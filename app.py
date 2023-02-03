from flask import Flask, request
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("model.h5")

classes = ['T-shirt', 'Trouser', 'Pullover', 'Dress','Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.route("/classify", methods=["POST"])
def classify():

    # Get the data from the request
    data = request.get_json()

    # Convert the data to a numpy array
    pixels = np.array(data["pixels"]).reshape(1, -1)

    # Use the model to make a prediction
    prediction = int(np.round(model.predict(pixels)[0][0]))

    # Return the result as a JSON response
    return {"class": str(prediction)}

if __name__ == "__main__":
    app.run()
