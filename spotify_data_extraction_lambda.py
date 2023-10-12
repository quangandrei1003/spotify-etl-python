import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime


def put_data_to_S3(bucket, data):
    client = boto3.client("s3")
    filename = "spotify_data_raw_" + str(datetime.now()) + ".json"

    return client.put_object(
        Bucket=bucket, Key="raw_data/to_processed/" + filename, Body=json.dumps(data)
    )


def lambda_handler(event, context):
    # TODO implement
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    top_today_list = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
    top_today_list_url = top_today_list.split("/")[-1]

    data = sp.playlist_tracks(top_today_list_url)
    put_data_to_S3("spotify-python-etl-quangnc", data)

    print(f"spotify data extaction lambda runs successfully at {datetime.now()}")
