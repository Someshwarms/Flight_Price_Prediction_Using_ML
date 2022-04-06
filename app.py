from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('Flight_Price_Prediction_Model1.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    Airline = float(request.form.get('Airline'))
    Source = float(request.form.get('Source'))
    Destination = float(request.form.get('Destination'))
    Total_Stops = float(request.form.get('Total_Stops'))
    Aditional_Info = float(request.form.get('Aditional_Info'))
    Journey_Day = float(request.form.get('Journey_Day'))
    Journey_Month = float(request.form.get('Journey_Month'))
    Journey_Year = float(request.form.get('Journey_Year'))
    Departure_hour = float(request.form.get('Departure_hour'))
    Departure_minute = float(request.form.get('Departure_minute'))
    Arrival_hour = float(request.form.get('Arrival_hour'))
    Arrival_minute = float(request.form.get('Arrival_minute'))
    Duration_hour = float(request.form.get('Duration_hour'))
    Duration_minute = float(request.form.get('Duration_minute'))


    result = model.predict(np.array([Airline,Source,Destination,Total_Stops,Aditional_Info,Journey_Day,Journey_Month,Journey_Year,Departure_hour,Departure_minute,Arrival_hour,Arrival_minute,Duration_hour,Duration_minute]).reshape(1, 14))

    return render_template('result.html', result=float(result))



if __name__ == '__main__':
    app.run(debug=True)