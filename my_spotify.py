from flask import session
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

import spotipy

    





def getTopTracksFromArtistList(artistList):

    # TODO: set limit of tracks per artist
    # BUG: some tracks belong to wrong artists? For example wtf is Elinaura?
    client_id = '707777b94d81455eb24e4e90a99a7a8c'
    client_secret = '7ab543121984470a86d80e8a0685e181'

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    allTopTracks = []
    # Loop through each artist and get their top tracks
    for artist_name in artistList:

        artist_name = artist_name.replace('\n', '').replace('\r', '')

        # BUG: dirty fix cause opener's website has incorrect spelling of some artists
        if artist_name == 'Pinkpantherees':
            artist_name = 'Pinkpantheress'


        # Search for the artist
        results = sp.search(q='artist:' + artist_name, type='artist')

        # TODO: make the reverse variable a parameter so you can end up with the most b-tec artists (parodies and almost the same name)
        # artistsSortedByPopularity = sorted(results['artists']['items'], key=lambda x: x['popularity'], reverse=True)
        
        if len(results['artists']['items']) > 0:
            artist = results['artists']['items'][0]
             # Get the artist's top tracks
            top_tracks = sp.artist_top_tracks(artist_id=artist['id'], country='US')
        
             # Print the artist's top tracks
            # print(artist_name + ':')

            for track in top_tracks['tracks']:
                 allTopTracks.append(track)
        
            ''

        


       

    return allTopTracks



# def authoriseSpotify():
    client_id = '707777b94d81455eb24e4e90a99a7a8c'
    client_secret = '7ab543121984470a86d80e8a0685e181'
    redirect_uri = 'http://localhost:5000/'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    username ='127342331'

    # Authenticate the client using the authorization code flow
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope='playlist-modify-private,playlist-modify-public',
                                                username=username))
    
    
    
def createPlaylistFromTopTracks(topTracks):
    
  
    
    token = session.get('access_token')
    sp = spotipy.Spotify(auth=token)

    user = sp.current_user()
    username = user['id']

    # Create a new playlist
    playlist_name = 'Custom Opener'
    playlist_description = 'beans beans beans'
    new_playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

    # Get the ID of the new playlist
    playlist_id = new_playlist['id']

    # Add some tracks to the new playlist
    track_uris = [track['uri'] for track in topTracks]

    # Split the track URIs into chunks of 100 to avoid Spotify errors
    chunks = [track_uris[i:i+100] for i in range(0, len(track_uris), 100)]
    
    # track_uris = ['spotify:track:7BAJpEXmYXQJ0wB1fLkS5k', 'spotify:track:2VlcoYEtFyoKW6YETFUW6B']
    for chunk in chunks:
        sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=chunk)
