from flask import Flask, render_template, request, redirect, url_for
import joblib

# Load the model
model = joblib.load('Random_Regression.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        try:
            # Receive the data
            screen_size = float(request.form['screenSize'])
            ram = int(request.form['ram'])
            weight = float(request.form['weight'])
            processor_speed = float(request.form['processorSpeed'])
            width = float(request.form['width'])
            height = float(request.form['height'])
            storage_capacity = int(request.form['storageCapacity'])
            gpu_code = int(request.form['gpuCode'])
            
            company = request.form["company"]
            type_ = request.form["type"]
            os = request.form["os"]
            generation = request.form["generation"]
            # series = request.form["series"]

            # Encode categorical variables
            companies = [
                'Acer', 'Apple', 'Asus', 'Chuwi', 'Dell', 'Fujitsu',
                'Google', 'HP', 'Huawei', 'LG', 'Lenovo', 'MSI',
                'Mediacom', 'Microsoft', 'Razer', 'Samsung', 'Toshiba',
                'Vero', 'Xiaomi'
            ]
            types = [
                '2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook',
                'Ultrabook', 'Workstation'
            ]
            oss = [
                'Android', 'Chrome OS', 'Linux', 'Mac OS X', 'No OS',
                'Windows 10', 'Windows 10 S', 'Windows 7', 'macOS'
            ]
            generations = [
                'Generation 1', 'Generation 3', 'Generation 5', 'Generation 7'
            ]
            # series_list = [
                # 'Series 0', 'Series A10', 'Series A12', 'Series A4',
        #    \.     'Series A6', 'Series A72', 'Series A8', 'Series A9'
            # ]

            def encode_categorical(value, categories):
                return [1 if category == value else 0 for category in categories]

            company_encoded = encode_categorical(company, companies)
            type_encoded = encode_categorical(type_, types)
            os_encoded = encode_categorical(os, oss)
            generation_encoded = encode_categorical(generation, generations)
            # series_encoded = encode_categorical(series, series_list)

            # Combine all inputs
            unseen_data = [[
                screen_size, ram, weight, processor_speed, width, height,
                storage_capacity, gpu_code
            ] + company_encoded + type_encoded + os_encoded + generation_encoded ]#+ series_encoded]

            # Make prediction
            prediction = float(model.predict(unseen_data)[0])

            return render_template('output.html', 
                                   output=prediction,
                                   screen_size=screen_size,
                                   ram=ram,
                                   weight=weight,
                                   processor_speed=processor_speed,
                                   width=width,
                                   height=height,
                                   storage_capacity=storage_capacity,
                                   gpu_code=gpu_code,
                                   company=company,
                                   type=type_,
                                   os=os,
                                   generation=generation)
                                #    series=series)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('error.html', error_message=error_message)

    return redirect(url_for('form'))

if __name__ == "__main__":
    app.run(debug=True)
