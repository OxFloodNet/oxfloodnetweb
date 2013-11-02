#!/usr/bin/env python
# @file views.py
#
# Routing for oxfloodnet

import flask
from httpcache import CachingHTTPAdapter
import requests

from oxfloodnet import oxfloodnet, calc

@oxfloodnet.route('/')
def index():
    """
    Return index HTML for human beings
    """
    return flask.render_template('index.html')

@oxfloodnet.route('/test/boundingbox/<centre>/<sw>/<ne>')
def return_request(**kwargs):
    """
    Return JSON data based on bounding box
    """
    request = dict([(i,calc.parse_latlon(j)) for (i,j) in kwargs.items()])
    return flask.json.jsonify(request = request)

@oxfloodnet.route('/data/<centre>/<sw>/<ne>')
def return_data(**kwargs):
    """
    Return JSON data based on bounding box
    """
    request = dict([(i,calc.parse_latlon(j)) for (i,j) in kwargs.items()])

    api_url = oxfloodnet.config['FLOOD_DATA_API_URL']
    params = {
        'lat': request['centre'][0],
        'lon': request['centre'][1],
        'radius': calc.best_circle_radius(
            request['centre'],
            request['sw'],
            request['ne']
        ),
        'api_key': oxfloodnet.config['FLOOD_DATA_API_KEY'],
    }
    s = requests.Session()
    s.mount('http://', CachingHTTPAdapter())
    s.mount('https://', CachingHTTPAdapter())
    r = s.get(api_url, params = params)
    return flask.json.jsonify(request = request, data = r.json())

@oxfloodnet.route('/test/distance/<a>/<b>')
def return_a_to_b(**kwargs):
    """
    Return JSON data giving a distance between two points
    """
    request = dict([(i,calc.parse_latlon(j)) for (i,j) in kwargs.items()])
    distance = calc.haversine(request['a'][1], request['a'][0], request['b'][1], request['b'][0])
    return flask.json.jsonify(request = request, distance = distance)

@oxfloodnet.errorhandler(calc.MalformedLatLon)
def handle_invalid_latlon(error):
    """
    Handle a badly formatted lat/lon comma-separated pair
    """
    response = flask.json.jsonify({"error": error.message})
    response.status_code = error.status_code
    return response
