from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to fetch country data from restcountries.com API
def get_country_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    country_data = None
    if request.method == 'POST':
        country_name = request.form['country_name']
        country_data = get_country_data(country_name)
    return render_template('index.html', country_data=country_data)

if __name__ == '__main__':
    app.run(debug=True)
