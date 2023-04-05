from flask import Flask, render_template, request

# __name__ is a special variable that is set to the name of the module in which it is used.
app = Flask(__name__)


@app.route('/')
def index():
    return """
        <h1>Search for an artist</h1>
        <form method="POST" action="/search">
            <input type="text" name="query" placeholder="Search for an artist...">
            <input type="submit" value="Search">
        </form>
    """


from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
    

client_id = '707777b94d81455eb24e4e90a99a7a8c'
client_secret = '7ab543121984470a86d80e8a0685e181'
redirect_uri = 'http://localhost/callback'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = sp.search(query, type='track')
    return render_template('results.html', results=results['tracks']['items'])


# check that this module is being run directly and not imported
if __name__ == '__main__':
    app.run(debug=True)


