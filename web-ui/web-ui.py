from bottle import Bottle, TEMPLATE_PATH
from bottle import run, post, get, template, static_file
from configparser import ConfigParser
from argparse import ArgumentParser
import os

abs_app_dir_path = os.path.dirname(os.path.realpath(__file__))
abs_views_path = os.path.join(abs_app_dir_path, 'views')
TEMPLATE_PATH.insert(0, abs_views_path )

app = Bottle()

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', default='config.ini',
    help='path to config (default: config.ini)')
parser.add_argument(
    '-p', '--path', required=True,
    help='path to static files')
args = parser.parse_args()

conf = ConfigParser()
conf.read(args.config)

host = conf.get('bottle', 'host')
port = conf.getint('bottle', 'port')

title = conf.get('site', 'title')

@app.route('/')
def start():
    return template('index', title=title)

@app.route('/static/<filename>')
def static(filename):
    return static_file(filename, root=args.path+"/static/")

run(app, host=host, port=port)
