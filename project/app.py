from flask import Flask, render_template
from weather import get_weather

app = Flask(__name__)

@app.route('/')
def home():
    weather_data = get_weather()

    return render_template(
        'index.html',
        city=weather_data['city'],
        temperature=weather_data['temperature'],
        humidity=weather_data['humidity'],
        condition=weather_data['condition']
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
