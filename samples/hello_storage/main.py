import json
import os

from datetime import datetime

from flask import jsonify
from google.cloud import storage

storage_client = storage.Client()

def hello_storage(request):
  payload = request.get_json(silent=True)

  pokemonId = payload['pokemonId']
  payload['created'] = datetime.utcnow().isoformat()
  payload_as_string = json.dumps(payload)

  bucket_name = os.getenv('BUCKET_NAME')
  bucket = storage_client.bucket(bucket_name)

  new_blob = bucket.blob(f'pokemons/pokemon-{pokemonId}.json')
  new_blob.upload_from_string(payload_as_string)

  return jsonify({ 'ok': 42 })
