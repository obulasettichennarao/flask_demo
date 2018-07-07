from flask_restplus import Resource
from http import HTTPStatus
from api import rest
from api.models import pr_status_output
import json
import requests
ns = rest.namespace('Pull_Requests', path='/', description='github pull request operations')


@ns.route('/Pull_requests/<string:owner>/<string:repo_name>')
class PullRequests(Resource):
    @ns.marshal_with(pr_status_output, as_list=True)
    def get(self, owner, repo_name):
        '''Returns a PRs and status for a given Branch
        GIT Repo : 'https://api.github.com/repos/obulasettichennarao/flask_demo/pulls'
        return {"prs_list": [{"pr_status": "open", "pr_id": 199891177}]}
        '''
        response = requests.get('https://api.github.com/repos/{owner}/{repo_name}/pulls'.format(owner=owner, repo_name=repo_name))
        data = response.json()

     
        class outobj:
            rows  = data  

        return outobj, HTTPStatus.OK
