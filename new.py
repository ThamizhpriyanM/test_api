import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        API_KEY = "f1e2a29b28485842a1ae7130b3d4ed62"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            current_temp = data['main']['temp']
            feels_like_temp = data['main']['feels_like']
            humidity = data['main']['humidity']
            return render_template('weather.html', city=city, weather=weather_description, 
                                   temp=current_temp, feels_like=feels_like_temp, humidity=humidity)
        else:
            return render_template('weather.html', error="City not found")
    else:
        return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)
