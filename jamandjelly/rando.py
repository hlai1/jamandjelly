'''
This file includes all the logic for playlist generation. It takes in a list of the
user's favorite artist, genre, and current mood and goes through the Spotify API to 
generate a playlist or a new playlist based on the user's last generated playlist.
'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import math

#spotify request information
client_id="e58bbc5d160f49aa942691aa1a50ecde"
client_secret="64e2b4f2593a49d88113025584e8cf1e"

#AUTH, POST, access token formatting, and getTrackFeatures function cited from: https://stmorse.github.io/journal/spotify-api.html
AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': "e58bbc5d160f49aa942691aa1a50ecde",
    'client_secret': "64e2b4f2593a49d88113025584e8cf1e",
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  artist = meta['album']['artists'][0]['name']

  # features we keep track of
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  loudness = features[0]['loudness']
  tempo = features[0]['tempo']
  valence = features[0]['valence']

  track = [name, artist, danceability, acousticness, energy, instrumentalness, valence, tempo, loudness]
  return track

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

#logic behind selectionSort method adapted from cmu 112 course website: https://www.cs.cmu.edu/~112/notes/notes-efficiency.html
def selectionSort(a):
    n = len(a)
    for startIndex in range(n):
        minIndex = startIndex
        for i in range(startIndex+1, n):
            artist, title, score = a[i]
            a1, t1, s1 = a[minIndex]
            if (score < s1):
                minIndex = i
        swap(a, startIndex, minIndex)
    return a

#getTrackIDs function below adapted from: https://betterprogramming.pub/how-to-extract-any-artists-data-using-spotify-s-api-python-and-spotipy-4c079401bc37

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

kpopList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/3kwb1LyzCSsLLacppOJQc8?si=6c264c5ab1724682')
latinList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/37i9dQZF1DXbLMw3ry7d7k?si=001a76d47b3740ab')
indieList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/37i9dQZF1DWWEcRhUVtL8n?si=e473463bfdde4054')
classList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/1h0CEZCm6IbFTbxThn6Xcs?si=f113b3355865403e')
popList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/37i9dQZF1DXbYM3nMM0oPk?si=d48e531605bf4bcc')
elecList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/37i9dQZF1EQp9BVPsNVof1?si=af4505da5bb94cf3')
hipHopList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/0FAb3s3yJArWnikZbEOO9p?si=4355ee417fe44baf')
countryList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/7d85RPHimZb0gR4PlY3IKq?si=bf90d3b9d0a44b9f')
holidayList = getTrackIDs('starfruit', 'https://open.spotify.com/playlist/37i9dQZF1DX0Yxoavh5qJV?si=7491dc0b582b4839')


#code below regarding sp.search, sp.artist, getTrackFeatures, track_id, etc. adapted from: https://pythonrepo.com/repo/plamere-spotipy-python-third-party-apis-wrappers
#other code in this function that doesn't involve grabbing data from spotify is written by me

def makeList(favArtist, favGenre, currMood, ctSong, currList, delList, charMatrix, sortedMat, titleList, subMatrix, o, upperLimit, i):
    if (len(currList) == ctSong):
        return currList
    else: 
        while (isinstance(favArtist, str) and (len(currList)) < ctSong):
            results = sp.search(q = favArtist, limit = upperLimit, offset = o)       
            for song, track in enumerate(results['tracks']['items']):
                artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
                if ((favGenre not in artist["genres"] or currMood == "holiday") and len(subMatrix) < ctSong//2):
                    if (currMood == "holiday"):
                        ids = holidayList
                    elif (favGenre == "kpop"):
                        ids = kpopList
                    elif(favGenre == "latin"):
                        ids = latinList
                    elif(favGenre == "indie"):
                        ids = indieList
                    elif(favGenre == "classical"):
                        ids = classList
                    elif(favGenre == "pop"):
                        ids = latinList
                    elif(favGenre == "electronic"):
                        ids = elecList
                    elif(favGenre == "hiphop"):
                        ids = hipHopList
                    elif(favGenre == "country"):
                        ids = countryList
                    track = getTrackFeatures(ids[i])
                    toAdd = (track[0], track[1])
                    i += 1
                    subMatrix.append(toAdd)
                else: 
                    BASE_URL = 'https://api.spotify.com/v1/'
                    track_id = track['id']

                    track = getTrackFeatures(track_id)

                    difference = 100

                    if (track[6] > 0.5): #happy song
                        if (currMood == "happy"):
                            difference = abs(track[6]-0.5)
                    if(track[6] < 0.5):
                        if (currMood == "sad"):
                            difference = abs(track[6]-0.5)
                    if(track[5] > 0.5):
                        if (currMood == "study"):
                            difference = abs(track[5]-0.5)
                    if(track[4] > 0.5 and track[7] > 120):
                        if (currMood == "angry"):
                            difference = abs(track[4]-0.5) + abs(track[7]-120)
                    if(track[8] > 0.5 and track[4] > 0.5):
                        if (currMood == "workout"):
                            difference = abs(track[8]-0.5) + abs(track[4]-0.5)
                    if(track[3] > 0.5 and track[4] > 0.5):
                        if (currMood == "party"):
                            difference = abs(track[3]-0.5) + abs(track[4]-0.5)
                    toAdd = (track[0], track[1], difference)
                    if (track[0] not in titleList):
                        titleList.append(track[0])
                        charMatrix.append(toAdd)
                    newAdd = (track[0], track[1])
                    if (i >= 5 and len(currList) < ctSong and delList != [] and newAdd not in currList and newAdd not in delList):
                        newAdd = (track[0], track[1])
                        currList.append(newAdd)
                        
            charMatrix = selectionSort(charMatrix)
            finalList = []
            for j in range(len(subMatrix)):
                if (subMatrix[j] not in currList and subMatrix[j] not in delList and len(currList) < ctSong):
                    currList.append(subMatrix[j])
                addedOtherGenre = True
            for i in range(ctSong-len(subMatrix)):
                x, y, z = charMatrix[i]
                adding = (x,y)
                if (adding not in currList and adding not in delList and len(currList) < ctSong):
                    currList.append(adding)
            return makeList(favArtist, favGenre, currMood, ctSong, currList, delList, charMatrix, sortedMat, titleList, subMatrix, o, upperLimit, i+1)

#code below regarding sp.search, sp.artist, getTrackFeatures, track_id, etc. adapted from: https://pythonrepo.com/repo/plamere-spotipy-python-third-party-apis-wrappers
#other code in this function that doesn't involve grabbing data from spotify is written by me
def makeGraph(L):
    print("generating 'random' playlist ")
    finalLen = len(L)
    newList = []
    songAssoc = {}
    newSong = {}
    for title, artist in L:
        results = sp.search(q = artist, limit = 5)
        currList = []
        for song, track in enumerate(results['tracks']['items']):
                artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
                BASE_URL = 'https://api.spotify.com/v1/'
                track_id = track['id']
                track = getTrackFeatures(track_id)
                toAdd = (track[0], track[1])
                if (toAdd not in L):
                    currList.append(track[0])
                key = track[1]
        songAssoc[key] = currList #dictionary of artists and 5 of their songs
    
    for key in songAssoc:
        for elem in songAssoc[key]:
            if elem in newSong:
                x, y = newSong[elem]

                newSong[elem] = (x+1, y)
            else:
                adding = (1, key)
                newSong[elem] = adding

    maxNum = len(L)//2
    while (maxNum > 0):
        for element in newSong:
            m, n = newSong[element]
            if (m == maxNum and element not in newList and len(newList) < len(L)):
                addTup = (element, n)
                newList.append(addTup)
        maxNum -= 1
    return newList