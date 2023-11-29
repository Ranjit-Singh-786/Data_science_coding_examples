from flask import Flask,render_template,url_for,request,jsonify
app = Flask(__name__)

# Defining Home route
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

# Defining a root called dharm
@app.route('/dharm',methods=['GET','POST'])
def dharm():
    return "Dharm asking ,,how are you  second time"
### ACCESSING PATH OF THIS ROUTE -->  http://localhost:8080/dharm


# Defining a root called jyoti
@app.route('/jyoti',methods=['GET','POST'])
def jyoti():
    return "jyoti asking ,,how are you  second time"
### ACCESSING PATH OF THIS ROUTE -->  http://localhost:8080/dharm


# Defining a root called aout
@app.route('/about',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        mobile = request.form['mobile']
        details = {'name':name+' '+surname,'Email':email,'mobile':mobile}
        return render_template('form_data.html',data=details)
    else:
        pass

# Defining a root called vinod
@app.route('/vinod',methods=['GET','POST'])
def vinod():
    return "Vinod asking ,,how are you ?"
### ACCESSING PATH OF THIS ROUTE -->  http://localhost:8080/vinod

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080",debug=True)