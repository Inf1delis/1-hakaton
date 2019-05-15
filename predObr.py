
from flask import Flask, request

from werkzeug import abort
from flask import Flask, request
import urllib.request
import json
from multiprocessing import Process
from server_routes import db
import os
import random
import string
from datetime import datetime
from time import sleep
import requests


app = Flask(__name__)
work_progs = ["chrome","pycharm","terminal"]
harm_progs = {"dota","telegram"}
active_progs = set([])
@app.route("/add_user", methods=['POST'])
def add_user():
    requests.post("http://localhost:8080",data =request.data )
    return "",200,{'Access-Control-Allow-Origin': '*'}
@app.route("/addInfo",methods = ['POST'])
def add_info():
    dataDict = request.data

    history_times = []
    history_progs = []

    efs_coef = ""
    for i in dataDict.get("active_history"):
        history_times.append(i.get("time"))
        history_progs.append(i.get(""))

    dataSend = {
        "surname":dataDict.get("surname"),
        "screenshot": dataDict.get("screenshot"),
        "photo":dataDict.get("photo"),
        "history":{ "values":history_times,
                    "labels":history_progs,
        },
        "efs":{ "x":dataDict("date"),
                "y":efs_coef
        },
        "clicks":{
                "date":dataDict.get("date"),
                "total": dataDict.get("clicks").get("total"),
                "right": dataDict.get("clicks").get("right"),
                "left": dataDict.get("clicks").get("left")
        }

    }

    return "",200,{'Access-Control-Allow-Origin': '*'}

# add info(data: datetime, active_history[{time:123, proc:str},{}],[,photo],[massiv] : [screencast])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, threaded=True)