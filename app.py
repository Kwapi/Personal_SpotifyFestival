import os
from flask import Flask, request, render_template, redirect, session, url_for

from artists import getOpenerArtists
from my_spotify import createPlaylistFromTopTracks, getTopTracksFromArtistList

# __name__ is a special variable that is set to the name of the module in which it is used.
app = Flask(__name__)
app.secret_key = 'H@McQfThWmZq4t7w!z%C*F-JaNdRgUkX'


artistsList = getOpenerArtists()


from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


# set up the SpotifyOAuth object with your app's client ID, client secret, and callback URL
client_id = '707777b94d81455eb24e4e90a99a7a8c'
client_secret='7ab543121984470a86d80e8a0685e181'
heroku_url = 'https://opener-playlist.herokuapp.com'
local_url = 'http://localhost:5000'


def get_base_url():
    if os.environ.get('APP_ENV') == 'production':
        return heroku_url
    else:
        return local_url



scope='user-library-read,playlist-modify-private,playlist-modify-public'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=get_base_url()+'/callback', scope=scope)

@app.route('/')
def index():
   
    # redirect the user to the Spotify authorization page
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # exchange the authorization code for an access token
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    session['access_token'] = access_token
    
    # redirect the user to the home page
    return redirect(url_for('artistList'))


# start site
@app.route('/artistList')
def artistList():
    return render_template('index.html',  artistsList = artistsList, authenticated=True)


@app.route('/chooseArtists', methods=['POST'])
def search():
    chosenArtists = request.form.getlist('chosenArtists[]')
    cleaned_list = [string.replace('\r', '').replace('\n', '') for string in chosenArtists]

    topTracks = getTopTracksFromArtistList(chosenArtists)
    createPlaylistFromTopTracks(topTracks)
    return render_template('results.html', topTracks = topTracks)



# check that this module is being run directly and not imported
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
  



