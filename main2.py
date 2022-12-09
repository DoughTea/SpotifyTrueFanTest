#!/usr/bin/env python
from flask import Flask, render_template, request
from rauth import OAuth1Service
import logging, json, urllib

app = Flask(__name__)

def get_day_data(lat=47.653465,lng=-122.307522,date=None,formatted=0):
    baseurl = 'https://api.sunrise-sunset.org/json'
    pdict = {
        "lat":lat,
        "lng":lng,
        "formatted":formatted
    }
    if date is not None:
        pdict['date'] = date
    paramstr = urllib.parse.urlencode(pdict)
    sunrequest = "%s?%s"%(baseurl,paramstr)
    sundata = urllib.request.urlopen(sunrequest)
    return json.load(sundata)

def get_day_data_safe(lat=47.653465,lng=-122.307522,date=None,formatted=0):
    try:
        return get_day_data(lat,lng,date,formatted)
    except urllib.error.HTTPError as e:
        app.logger.error("Error trying to retrieve data: %s"%e)
    except urllib.error.URLError as e:
        app.logger.error("We failed to reach a server.")
        app.logger.error("Reason: ", e.reason)
    return None

@app.route("/")
def main_handler():
    app.logger.info("In MainHandler")
    loc = request.args.get('loc')
    if loc:
        ll = loc.split(",")
        lat=ll[0]
        lng=ll[1]
        date = request.args.get('date')
        # if form filled in, greet them using this data
        sunrisesunsetdata = get_day_data_safe(lat,lng,date)
        if sunrisesunsetdata is not None:
            title = "Sunrise Sunset data for %s"%loc
            if date: title += " on %s"%date
            return render_template('sunrisesunsettemplate.html',
                page_title=title,
                sunrisesunsetdata=sunrisesunsetdata
                )
        else:
            return render_template('sunrisesunsettemplate.html',
                page_title="Sunrise Sunset Form - Error",
                prompt="Something went wrong with the API Call")                  
    elif loc=="":
        return render_template('sunrisesunsettemplate.html',
            page_title="Sunrise Sunset Form - Error",
            prompt="We need a location")
    else:
        return render_template('sunrisesunsettemplate.html',page_title="Sunrise Sunset Form")

if __name__ == "__main__":
    # Used when running locally only. 
	# When deploying to Google AppEngine or PythonAnywhere,
    # a webserver process will serve your app. 
    app.run(host="localhost", port=8080, debug=True)#!/usr/bin/env python
from flask import Flask, render_template, request
import logging, json, urllib

app = Flask(__name__)

def get_day_data(lat=47.653465,lng=-122.307522,date=None,formatted=0):
    baseurl = 'https://api.sunrise-sunset.org/json'
    pdict = {
        "lat":lat,
        "lng":lng,
        "formatted":formatted
    }
    if date is not None:
        pdict['date'] = date
    paramstr = urllib.parse.urlencode(pdict)
    sunrequest = "%s?%s"%(baseurl,paramstr)
    sundata = urllib.request.urlopen(sunrequest)
    return json.load(sundata)

def get_day_data_safe(lat=47.653465,lng=-122.307522,date=None,formatted=0):
    try:
        return get_day_data(lat,lng,date,formatted)
    except urllib.error.HTTPError as e:
        app.logger.error("Error trying to retrieve data: %s"%e)
    except urllib.error.URLError as e:
        app.logger.error("We failed to reach a server.")
        app.logger.error("Reason: ", e.reason)
    return None

@app.route("/")
def main_handler():
    app.logger.info("In MainHandler")
    loc = request.args.get('loc')
    if loc:
        ll = loc.split(",")
        lat=ll[0]
        lng=ll[1]
        date = request.args.get('date')
        # if form filled in, greet them using this data
        sunrisesunsetdata = get_day_data_safe(lat,lng,date)
        if sunrisesunsetdata is not None:
            title = "Sunrise Sunset data for %s"%loc
            if date: title += " on %s"%date
            return render_template('sunrisesunsettemplate.html',
                page_title=title,
                sunrisesunsetdata=sunrisesunsetdata
                )
        else:
            return render_template('sunrisesunsettemplate.html',
                page_title="Sunrise Sunset Form - Error",
                prompt="Something went wrong with the API Call")                  
    elif loc=="":
        return render_template('sunrisesunsettemplate.html',
            page_title="Sunrise Sunset Form - Error",
            prompt="We need a location")
    else:
        return render_template('sunrisesunsettemplate.html',page_title="Sunrise Sunset Form")

if __name__ == "__main__":
    # Used when running locally only. 
	# When deploying to Google AppEngine or PythonAnywhere,
    # a webserver process will serve your app. 
    app.run(host="localhost", port=8080, debug=True)