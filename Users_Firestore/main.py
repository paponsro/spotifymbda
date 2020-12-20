import json
import os

from datetime import datetime
from random import randint

from flask import jsonify
from google.cloud import firestore

db = firestore.Client()

def users_firestore(request):
  payload = request.get_json(silent=True)
  email=payload ['email']
  name = payload['name']
  age = payload ['age']
  
  doc_ref = db.collection('users').document()
  doc_ref.set({
    'email': email,
    'name': name,
    'age': age,
    
    
  })

  return jsonify({ 'ok': 42, 'externalId': doc_ref.id })
  