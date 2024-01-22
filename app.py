from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde Railway en Python!'


@app.route('/XD')
def XD():
    return render_template('XD.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))