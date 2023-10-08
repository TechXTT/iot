from flask import Flask, render_template
from utils.utils import get_temperatures, get_highest_average_temperature

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

# Returns a generated image of the temperatures for January
@app.route('/temperatures', methods=['GET'])
def display_png():
    with open('static/temperatures.csv', 'r') as f:
        image_filename = get_temperatures(f)

        return render_template('temperatures.html', image_filename=image_filename)

# Returns the room with the highest average temperature for January
@app.route('/highest', methods=['GET'])
def highest_average_temperature():
    with open('static/temperatures.csv', 'r') as f:
        return {'highest_average_temperature': get_highest_average_temperature(f)}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)