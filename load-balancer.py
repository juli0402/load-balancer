from flask import Flask, request
import requests, random

loadbalancer = Flask(__name__)

LISTAPP_BACKENDS = ["", ""]
BUSCAPP_BACKENDS = ["", ""]

@loadbalancer.route('/')
def router():
    host_header = request.headers["Host"]
    if host_header == "listapp/":
        response = requests.get("http://{}".format(random.choice(LISTAPP_BACKENDS)))
        return response.content, response.status_code
    elif host_header == "buscapp/":
        response = requests.get("http://{}".format(random.choice(BUSCAPP_BACKENDS)))
        return response.content, response.status_code
    else:
        return "Not Found", 404

@loadbalancer.route('/listapp')
def listapp_path():
    response = requests.get("http://{}".format(random.choice(LISTAPP_BACKENDS)))
    return response.content, response.status_code

@loadbalancer.route('/buscapp')
def buscapp_path():
    response = requests.get("http://{}".format(random.choice(BUSCAPP_BACKENDS)))
    return response.content, response.status_code