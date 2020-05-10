from flask import Flask, render_template, url_for, request, redirect, jsonify
import COVID19Py


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/updates', methods=["GET", "POST"])
def updates():
        option = request.form['op']
        covid19 = COVID19Py.COVID19()
        location = covid19.getLocationByCountryCode({option})
        return jsonify(location)

       

        
        

        
        
        

if __name__ == "__main__": 
        app.run(debug=True)