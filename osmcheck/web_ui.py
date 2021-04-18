import math
import os

import urllib.parse

from bottle import Bottle, TEMPLATE_PATH
from bottle import run, post, get, template, static_file
from argparse import ArgumentParser

from osmcheck import api

from .web_jodel import hr

from .conf import (
    DEFAULT_REGION, DEFAULT_CITY,
    WEB_TITLE, WEB_HOST, WEB_PORT,
    JODEL_DEFAULT_CHANNEL
)


abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, "views")
TEMPLATE_PATH.insert(0, abs_views_path)

app = Bottle()
app.mount("/jodel", hr)


@app.route("/")
def start():
    return template("index", title=WEB_TITLE)


@app.route("/inventory/<page:int>")
def inventory(page):
    page = max(0, page)
    all_entries = api.query_osm(DEFAULT_REGION)
    pages_max = math.floor(len(all_entries) / 15)

    entries = all_entries[page*15:(page+1)*15]
    items = [{"entry": e, "score": api.calc_score(e)} for e in entries]
    return template("inventory", title=WEB_TITLE,
                    city=DEFAULT_CITY, items=items,
                    page=page, pages_max=pages_max,
                    jodel_channel=JODEL_DEFAULT_CHANNEL,
                    quote=urllib.parse.quote_plus)


@app.route("/analysis")
def analysis():
    return template("analysis", title=WEB_TITLE)


@app.route("/static/<filename>")
def static(filename):
    return static_file(filename, root="osmcheck/static/")


run(app, server="waitress", host=WEB_HOST, port=WEB_PORT)
