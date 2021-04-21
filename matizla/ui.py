from flask.helpers import send_from_directory
from matizla.assets import LoadingScreen
from webview.window import Window
from matizla.api import MatizlaWebApi
import webview
import platform
from time import sleep
from flask import Flask, render_template

""" Main window flask stuff """
from matizla.assets import MainScreen

main_window_server = Flask(
    __name__,
    static_folder=MainScreen.__path__[0],
    template_folder=MainScreen.__path__[0]
)
main_window_server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1


@main_window_server.route('/')
def loadingIndex():
    return render_template('index.html')


""" Loading window flask stuff """

loading_window_server = Flask(
    __name__,
    static_folder=LoadingScreen.__path__[0],
    template_folder=LoadingScreen.__path__[0],
    static_url_path=''
)
loading_window_server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1


@loading_window_server.route('/')
def loadingIndex():
    return render_template('index.html')

@main_window_server.after_request
@loading_window_server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

MAIN_WINDOW: Window = webview.create_window(
    "main",
    main_window_server,
    width=800,
    height=480,
    resizable=False,
    fullscreen=(platform.machine() == "armv7l"),
    on_top=False,
    js_api=MatizlaWebApi()
)
LOAD_WINDOW: Window = webview.create_window(
    "main",
    loading_window_server,
    width=800,
    height=480,
    resizable=False,
    fullscreen=(platform.machine() == "armv7l"),
    on_top=True,
    transparent=False
)


def close():
    for w in webview.windows:
        w.destroy()


def start(func):
    MAIN_WINDOW.closed += close
    LOAD_WINDOW.closed += close

    webview.start(debug=True, func=func)
