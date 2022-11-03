from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_jokes import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/faq')

responses = []  # responses list

    # get count of jokes on server
count_response = requests.get(url+"/count")
count_json = count_response.json()
count = count_json['count']

    # update likes/dislikes test sequence
num = str(random.randint(0, count-1)) # test a random record
responses.append(
    requests.get(url+"/"+num)  # read joke by id
    ) 
responses.append(
    requests.put(url+"/like/"+num) # add to like count
    ) 
responses.append(
    requests.put(url+"/jeer/"+num) # add to jeer count
    ) 

    # obtain a random joke
responses.append(
    requests.get(url+"/random")  # read a random joke
    ) 

    # cycle through responses
for response in responses:
    print(response)
    try:
        print(response.json())
    except:
        print("unknown error")