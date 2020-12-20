import json
import os

from datetime import datetime
from random import randint

from flask import jsonify
from google.cloud import firestore


import "google/protobuf/duration.proto";
import "google/protobuf/timestamp.proto";
db = firestore.Client()

def events_firestore(request):
  payload = request.get_json(silent=True)
  resource_id=payload ['id']
  resource_name = payload['name']
  category_id = payload ['categoryId']
  provider_id = payload ['providerId']
  promotion = payload ['promotion']

  doc_ref = db.collection('events').document()
  doc_ref.set({
    'resource_id': resource_id,
    'resource_name': resource_name,
    'category_id': category_id,
    'provider_id': provider_id,
    'promotion' : promotion,
    
  })

  return jsonify({ 'ok': 42, 'externalId': doc_ref.id })
  