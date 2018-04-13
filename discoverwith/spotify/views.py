import base64
import requests
from urllib.parse import urlencode

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

client_id = ''
client_secret = ''

def go_to_spotify_for_auth(req):
	return HttpResponseRedirect('https://accounts.spotify.com/en/authorize?{}'.format(
		urlencode(
			{
				'client_id': client_id,
				'redirect_uri': 'http://localhost:8000/auth/receive-redirect',
				'response_type': 'code',
				'scopes': 'playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative',
				'state': 'somestate'
			}
		)
	))

def receive_redirect_refresh(req):
	return HttpResponse("Hello world")

def receive_redirect(req):
	auth_code = req.GET['code']
	state_value = req.GET['state']

	client_stuff = '{}:{}'.format(client_id, client_secret)
	clientb64 = base64.b64encode(client_stuff.encode('utf-8')).decode('utf-8')

	print(clientb64)
	print('Basic ' + clientb64)

	resp = requests.post(
		"https://accounts.spotify.com/api/token",
		{
			'grant_type': 'authorization_code',
			'code': auth_code,
			'redirect_uri': 'http://localhost:8000/auth/receive-redirect'
		},
		headers={
			'Authorization': 'Basic ' + clientb64,
		},
	)

	print(resp)

	return HttpResponse(resp.content)
