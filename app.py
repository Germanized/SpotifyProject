from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch_songs")
def fetch_songs():
    url = "https://spotifycharts.com/regional/global/weekly/latest"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        song_elements = soup.find_all("tr", class_="chart-table-track")

        songs_html = ""
        for index, song_element in enumerate(song_elements, start=1):
            song_name = song_element.find("strong").get_text(strip=True)
            artist_name = song_element.find("span").get_text(strip=True)
            songs_html += f"<li><strong>{index}. {song_name}</strong> by {artist_name}</li>"

        return songs_html

    else:
        return "Failed to fetch data"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
