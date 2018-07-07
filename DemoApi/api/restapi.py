from flask import Blueprint
from flask_restplus import Api as Rest
api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
rest = Rest(
  api_blueprint,
  description='GIT Hub PullRequest status API',
  doc='/doc/',
  title='Git PR API',
  validate=True,
)
# Don't interpret a 404 as a badly formed URL, when it probably means "Record not found"
# By default, this appends a "Did you mean these URLs?" string to the status message
rest._help_on_404 = lambda message: message
