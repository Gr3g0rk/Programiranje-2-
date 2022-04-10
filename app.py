from logging import NullHandler
import shutil
from urllib import request
from flask import Flask, request
import os
from os import listdir
from os.path import isfile, join
#import numpy as np
#import cv2
#import base64
#from time import time
import json

app = Flask(__name__)

# Kratek izpis če se povežemo na ip API-ja
@app.route('/')
def index():
    return '<3 Mai + Gregi <3'

# POST metoda za API, ki vrača bounding box-e v obliki JSON, če mu podamo pot do slike
@app.route('/AllDrugSeizures', methods=['GET'])
def allDrugSeizuresF():
    f = open('DrugSeizures.json')
    data = json.load(f)
    return data


@app.route('/OverDose', methods=['GET'])
def OverDoseF():
    f = open('OverDose.json')
    data = json.load(f)
    return data


@app.route('/DrugSeizuresPost', methods=['POST'])
def DrugSeizuresPostF():
    f = open('DrugSeizures.json')
    data = json.load(f)["data"]

    Region = request.json['Region']
    Country = request.json['Country']
    Year = request.json['Year']
    DrugGroup = request.json['DrugGroup']
    Drug = request.json['Drug']
    Code = request.json['Code']

    newJson = {"data" : []}
    for el in data:
        if (Region == el['Region'] or not Region) and (Country == el['Country'] or not Country) and (Year == el['Year'] or not Year)  and (DrugGroup == el['DrugGroup'] or not DrugGroup)  and (Drug == el['Drug'] or not Drug)  and (Code == el['Code'] or not Code) :
            newJson["data"].append(el)

    json_object = json.dumps(newJson, indent = 4) 
    #val = request.json['val']
    return json_object