import requests
from bs4 import BeautifulSoup

def extract_headlines(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h3')
        return [h.text.strip() for h in headlines[:10]]
    except Exception as e:
        return [f"Error: {str(e)}"]
