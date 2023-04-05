from flask import Flask, render_template, request

from artists import getOpenerArtists
from my_spotify import getTopTracksFromArtistList

# __name__ is a special variable that is set to the name of the module in which it is used.
app = Flask(__name__)


# start site
@app.route('/')
def index():
    return """
        <h1>Search for an artist</h1>
        <form method="POST" action="/search">
            <input type="text" name="query" placeholder="Search for an artist...">
            <input type="submit" value="Search">
        </form>
    """


artistsList = getOpenerArtists()

topTracks = getTopTracksFromArtistList(artistsList)

@app.route('/search', methods=['POST'])
def search():
    # query = request.form['query']

    # resultsSearch = sp.search(query, type='artist')
    # artist = resultsSearch['artists']['items'][0]
    # results = sp.artist_top_tracks(artist_id=artist['id'], country='GB')


    return render_template('results.html', topTracks = topTracks)



# check that this module is being run directly and not imported
if __name__ == '__main__':
    app.run(debug=True)


