from flask import Flask, request, render_template, url_for
import joblib
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the trained model
model = joblib.load('best_random_forest_model.joblib')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tips')
def tips():
    return render_template('Tips.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        try:
            # Get form data
            form_data = request.form
            features = np.array([[int(form_data['male']), int(form_data['age']), int(form_data['education']),
                                int(form_data['cigsPerDay']), int(form_data['BPMeds']), int(form_data['prevalentStroke']),
                                int(form_data['prevalentHyp']), int(form_data['diabetes']), int(form_data['totChol']),
                                int(form_data['sysBP']), int(form_data['diaBP']), float(form_data['BMI']),
                                int(form_data['heartRate']), int(form_data['glucose'])]])

            # Predict CHD
            prediction = model.predict(features)
            prediction_proba = model.predict_proba(features)

            # Render the prediction result on the same page
            return render_template('prediction.html', prediction=prediction[0], probability=prediction_proba[0][1])
        except Exception as e:
            return str(e)
    else:
        return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)

