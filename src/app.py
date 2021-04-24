from flask import Flask, render_template, json
from pinger import Pinger
from configparser import ConfigParser
import _thread
import time

app = Flask(__name__,
            static_url_path='', 
            static_folder='../static',
            template_folder='../templates')
config = ConfigParser()
pinger = Pinger(config)

def update_values(): 
    while True:
        pinger.ping_all()
        time.sleep(config.get_check_interval())

@app.route('/')
def index():
    return render_template('index.html', title=config.get_name(), description=config.get_description(), icon=config.get_icon())

@app.route("/json")
def get_data():
    response = app.response_class(
        response=json.dumps(pinger.get_values()),
        status=200,
        mimetype='application/json'
    )
    return response

@app.before_first_request
def activate_job():
    try:
        _thread.start_new_thread(update_values, ())
    except:
        print("Error: unable to start thread")

if __name__ == '__main__':
    app.run()