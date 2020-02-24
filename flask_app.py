from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/about', methods=['GET'])
def mission():
    return render_template('about.html')

@app.route('/petition', methods=['GET'])
def petition():
    return render_template('petition.html')
