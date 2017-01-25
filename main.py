from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)


@app.route('/')
def calendar():
    return render_template("json.html")


@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    with open("events.json", "r") as input_data:
        return input_data.read()

if __name__ == '__main__':
    app.debug = True
    app.run()
