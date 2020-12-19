

import sys
from flask import escape


def resources_id (request):
  song = request.get_json(silent=True)

  song_id = song['id']
  song['externalId'] = datetime.utcnow().isoformat()
  song_as_string = json.dumps(song)

  bucket_name = os.getenv('BUCKET_NAME')
  bucket = storage_client.bucket(bucket_name)

  new_blob = bucket.blob(f'songs/song-{resource_id}.json')
  new_blob.upload_from_string(song_as_string)
  print(song)

  return song 

