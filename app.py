from flask import Flask, render_template, request
from scraper import extract_headlines

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    headlines = []
    if request.method == 'POST':
        url = request.form['url']
        headlines = extract_headlines(url)
    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
