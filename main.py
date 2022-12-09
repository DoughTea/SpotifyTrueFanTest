import requests
import json
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template, request
from rauth import OAuth1Service
import logging, json, urllib

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


app = Flask(__name__)

def get_song_data(search_term):
    client_access_token = "zfWrFxJwkxdCOTZDZ8rw3mi09_Yy6GFvVrro9-aElRzVcm0rThneQQrp9NSab7jt"

    search_term = search_term
    genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

    response = requests.get(genius_search_url)
    json_data = response.json()
    return json_data

def get_song_data_safe(search_term):
    try:
        return get_song_data(search_term)
    except urllib.error.HTTPError as e:
        app.logger.error("Error trying to retrieve data: %s"%e)
    except urllib.error.URLError as e:
        app.logger.error("We failed to reach a server.")
        app.logger.error("Reason: ", e.reason)
    return None

# print(pretty(json_data))

# json_data = get_song_data_safe("Kendrick Lamar")

# for song in json_data["response"]["hits"]:
#     songs.append([song["result"]["full_title"], song["result"]["release_date_components"]])

# print(songs)

# random.randint(0, b)


@app.route("/")
def main_handler():
    app.logger.info("In MainHandler")
    loc = request.args.get('loc')
    if loc:
        # if form filled in, greet them using this data
        songData = get_song_data_safe(loc)
        songs = []
        for song in songData["response"]["hits"]:
            songs.append([song["result"]["full_title"], song["result"]["release_date_components"]])
        if songData is not None:
            title = "Which one came out first for %s?"%loc
            return render_template('homepagetemplate.html',
                page_title=title,
                songData=songData
                )
        else:
            return render_template('homepagetemplate.html',
                page_title="Artist Form - Error",
                prompt="Something went wrong with the API Call")                  
    elif loc=="":
        return render_template('homepagetemplate.html',
            page_title="Artist Form - Error",
            prompt="We need a artist name to search for!")
    else:
        return render_template('homepagetemplate.html',page_title="Sunrise Sunset Form")

if __name__ == "__main__":
    # Used when running locally only. 
	# When deploying to Google AppEngine or PythonAnywhere,
    # a webserver process will serve your app. 
    app.run(host="localhost", port=8080, debug=True)#!/usr/bin/env python
from flask import Flask, render_template, request
