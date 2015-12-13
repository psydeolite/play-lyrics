import urllib2
import json
import spotipy
import spotipy.util as util
import requests
import base64

from spotipy.oauth2 import SpotifyClientCredentials

ci='clientid'
cs='clientsecret'

#replace with actual stuff
ccm=SpotifyClientCredentials(client_id='client-id', client_secret='client-secret')
token=ccm.get_access_token()
sp=spotipy.Spotify(auth=token)


def get_new_albums():
    ''' TRIED TO DO PLAYLISTS, TO NO AVAIL :'(
    plays=sp.featured_playlists(locale=None, country=None, timestamp=None, limit=20, offset=0)['playlists']['items']
    play1=plays[0]
    tracks=play1['tracks']
    url2=tracks['href']
    print url2
    url='https://accounts.spotify.com/api/token'
    print url
    global ci, cs
    unenc=ci+':'+cs
    enc=base64.b64encode(ci+':'+cs)
    global token
    params={'grant_type':'client_credentials'}
    
    r=requests.post(url, data=params, auth=(ci, cs))
    token2=r.json()['access_token']
    print token2
    headers={'Authorization':'Bearer '+token2}
    nr=requests.post(url2, headers=headers)
    print nr
    '''
    print 'INSIIIDE'
    data=sp.new_releases(country=None, limit=20, offset=0)
    albums_data=data['albums']['items']
    #print albums_data[0].keys()
    albums_uris=[]
    for album in albums_data:
        albums_uris.append(album['uri'])
    #print albums_uris

    albums_all=[]
    for uri in albums_uris:
        albinf={}
        albdat=sp.album(uri)
        trackdat=sp.album_tracks(uri,limit=50,offset=0)['items']
        tracks=[]
        for track in trackdat:
            track_meta={}
            track_meta['name']=str(track['name'])
            track_meta['artists']=str(track['artists'][0]['name'])            
            track_meta['uri']=str(track['uri'])
            tracks.append(track_meta)
        albinf['name']=str(albdat['name'])
        albinf['artists']=str(albdat['artists'][0]['name'])
        albinf['image']=str(albdat['images'][0]['url'])
        albinf['tracks']=tracks;
        albums_all.append(albinf)

    #print albums_all[0]
    return albums_all


#get_new_albums()
