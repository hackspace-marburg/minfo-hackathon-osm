from bottle import Bottle, TEMPLATE_PATH
from bottle import run, post, get, template, static_file
from argparse import ArgumentParser
import os

from osmcheck import api

from .conf import DEFAULT_REGION, WEB_TITLE, WEB_HOST, WEB_PORT


abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, "views")
TEMPLATE_PATH.insert(0, abs_views_path)

app = Bottle()


@app.route("/")
def start():
    return template("index", title=WEB_TITLE, page=start)


@app.route("/inventory")
def inventory():
    entries = api.query_osm(DEFAULT_REGION)[:15]
    items = [{"entry": e, "score": api.calc_score(e)} for e in entries]
    return template("inventory", title=WEB_TITLE, items=items, page=inventory)


@app.route("/analysis")
def analysis():
    return template("analysis", title=WEB_TITLE, page=analysis)


@app.route("/static/<filename>")
def static(filename):
    return static_file(filename, root="osmcheck/static/")


run(app, host=WEB_HOST, port=WEB_PORT)
