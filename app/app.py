from flask import Flask, request, jsonify
from loguru import logger
import random
import requests
import time
import config

app = Flask(__name__)

#logger
logger.add("app.log",rotation="2 MB",retention="7 days",level="INFO")

# get_ip
@app.route('/my-ip', methods=['GET'])
def myip():
    ip_add = request.remote_addr
    #return ip_add
    return jsonify({"ip":ip_add})


# qoute
@app.route('/qoute', methods=['GET'])
def qoute():
    qoutes = [
        "It is never too late to be what you might have been.", "Do one thing every day that scares you.",
        "Nothing is impossible. The word itself says ‘I’m possible!’",
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "Success is falling nine times and getting up ten.",
        "You miss 100% of the shots you don’t take.",
        "A problem is a chance for you to do your best.",
        "Dreams do not come true just because you dream them. It’s hard work that makes things happen.",
        "If you change the way you look at things, the things you look at change.",
        "Life has got those twists and turns. You’ve got to hold on tight and off you go.",

    ]
    logger.info(f'Qoute API run at {time.time()}:')
    #return random.choice(qoutes)
    return jsonify(random.choice(qoutes))


# weathr
weater_api_key = config.weather_api_key
base_url = "https://api.openweathermap.org/data/2.5/weather"
@app.route('/weather', methods=['POST'])
def weather():
    body_data = request.get_json()
    print("DEBUG body_data:", body_data)
    city = body_data.get('city')
    url = f'{base_url}?appid={weater_api_key}&q={city}'
    if not city:
        return jsonify({"error": "Please enter a city name."}), 400
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify(f'Could not fetch weather data.Check the URL and try again.'), response.status_code
    else:
        data = response.json()
        weather_info = {
            "city": data.get('name'),
            "temperature": data.get('main', {}).get('temp'),
            "humidity": data.get('main', {}).get('humidity')
        }
        return jsonify(weather_info)


if __name__ == '__main__':
    app.run(debug=True)
