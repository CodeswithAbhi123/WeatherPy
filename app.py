from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '578e5c8c9dc63748953a98295e02e947'  
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    weather_data = response.json()
    
    if weather_data['cod'] == 200:
        weather_info = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed']
        }
    else:
        weather_info = None
    
    return render_template('weather.html', weather=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
