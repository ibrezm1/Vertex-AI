import pandas as pd
from flask import Flask, jsonify,request
import tensorflow as tf
from customprocessing import preprocess,postprocess

app = Flask(__name__)

model = tf.keras.models.load_model('model')

@app.route('/predict',methods=['POST','GET'])
def predict():
    req = request.json.get('instances')
    #req = list(req)
    input_data = [ r['email'] for r in req ]  

    #preprocessing
    preprocessed_text_arr = [ preprocess(t) for t in input_data ] 
    #vector = pre_process.preprocess_tokenizing(text)


    #predict
    prediction = model.predict(preprocessed_text_arr)

    #postprocessing
    out = [ postprocess(t) for t in prediction  ]
    output = {'predictions': out }
    return jsonify(output)

@app.route('/healthz',methods=['POST','GET'])
def healthz():
    return "OK"

    


if __name__=='__main__':
    app.run(host='0.0.0.0')

