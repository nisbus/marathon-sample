from flask import Flask, jsonify, Blueprint
from flask_restplus import Resource, Api
import requests
import os

app = Flask(__name__)
api = Api(app, version="1.0", title="Marathon sample app")
marathonBaseUrl = os.environ.get('MARATHON_HOST', 'http://localhost:8080')
cmd = '#!/bin/bash while true do echo "sleeping" sleep 1 done'


@api.route('/api/', methods=['GET'])
class AppListResource(Resource):
	""""
	Resource for returning a list of running apps in Marathon
	"""

	@staticmethod
	def get():
		"""
		Gets a list of all apps running in Marathon

		Returns
		-------
		A list of all apps running in Marathon
		"""
		url = AppResource.create_url()
		return AppResource.create_response('get', requests.get(url))


@api.route('/api/<app_id>', methods=['GET', 'DELETE', 'POST'], doc={'params': {'app_id': 'the app id'}})
class AppResource(Resource):
	"""
	Simple api to start a useless application in Marathon
	"""

	@staticmethod
	def get(app_id):
		"""
		Get a single app from Marathon identified by the app_id

		Parameters
		----------
		app_id : The Id of the app to get

		Returns
		-------
		200 with the app information if it exists, otherwise the error message received from marathon
		"""
		url = AppResource.create_url(app_id)
		return AppResource.create_response('get', requests.get(url))

	@staticmethod
	def delete(app_id):
		"""
		Stops an existing app in Marathon identified by app_id

		Parameters
		----------
		app_id: The Id of the app to stop

		Returns
		-------
		200 on successful delete, otherwise the error message received from marathon
		"""
		url = AppResource.create_url(app_id)
		return AppResource.create_response('delete', requests.delete(url))

	@staticmethod
	def post(app_id):
		"""
		Starts a new app identified by the app_id

		Parameters
		----------
		app_id: the app_id used to identify the new app

		Returns
		-------
		200 on a successful start, otherwise the error message received from marathon
		"""
		url = AppResource.create_url()
		return AppResource.create_response('post', requests.post(url, json={'id': app_id, 'cmd': cmd}))

	@staticmethod
	def create_response(method, response):
		"""
		Parses the response to Marathon and creates a response for the API
		:param method: The HTTP method being called
		:param response: The response received from Marathon
		:return: A JSON message to return from the API
		"""
		if (method == 'post' and response.status_code == 201) or \
			(method == 'delete' and response.status_code == 204):
			return {'message': 'request sent to marathon'}
		return response.json(), response.status_code

	@staticmethod
	def create_url(app_id=None):
		"""
		Formats the url to call depending on whether there is an app_id parameter in the request
		:param app_id: The id of the app being requested
		:return: An url for the call to Marathon
		"""
		if app_id:
			return '{}/v2/apps/{}'.format(marathonBaseUrl, app_id)
		else:
			return '{}/v2/apps'.format(marathonBaseUrl)


if __name__ == '__main__':
	"""
	Starts the API if run from console
	"""
	app.run(host='0.0.0.0')
