from flask import Flask, render_template, request
import joblib
import re
from emaildata import init_db, insert_prediction, close_connection

# Load the model and CountVectorizer
model = joblib.load('models/multinomialnaivebayes.lb')
bow_obj = joblib.load('models/countvectorizer.lb')

# Initialize Flask app
app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):  # Accept the exception argument
    close_connection(exception)  # Pass it to the close_connection function

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        emailContent = request.form.get('emailContent', '')
        emailContent = emailContent.lower()
        emailContent = re.sub(r'[^a-zA-Z ]', '', emailContent)

        emailContent_transformed = bow_obj.transform([emailContent])
        prediction = model.predict(emailContent_transformed)[0]

        labels = {'1': "SPAM", '0': "HAM"}
        result = labels.get(str(prediction))

        # Store the prediction in the database
        insert_prediction(emailContent, result)

        return render_template('home.html', output=result)

if __name__ == "__main__":
    init_db(app)  # Pass the app instance to initialize the database with the table
    app.run(debug=True)
