import json
import os

from datetime import datetime
from random import randint

from flask import jsonify
from google.cloud import firestore

db = firestore.Client()

def hello_firestore(request):
  payload = request.get_json(silent=True)
  pokemonId = payload['pokemonId']

  doc_ref = db.collection('pokemon').document(pokemonId)
  doc_ref.set({
    'pokemonId': pokemonId,
    'level': randint(0,10),
    'created': datetime.utcnow().isoformat()
  })

  return jsonify({ 'ok': 42 })
