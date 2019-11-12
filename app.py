
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
url = "https://api.openweathermap.org/data/2.5/weather"
@app.route('/')
def weather():
    return render_template('/weather.html')

@app.route('/results')
def weather_results():
    cityName = request.args.get('city')

    params = {
        'q': cityName,
        'appid': 'e650c50fb0a09fc43853456d5f75d73e'
    }

    response = requests.get(url, params=params)
    results = response.json()

    city = results['name']
    temp = conversion(results['main']['temp'])

    return render_template('results.html', city=city, temp=temp)

def conversion(kelvin):
    convert = 1.8 * (kelvin-273) + 32
    return int(convert)

if __name__ == '__main__':
    app.run()
