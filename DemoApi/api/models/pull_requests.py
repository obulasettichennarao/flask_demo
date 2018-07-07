import marshmallow as m
from flask_restplus import fields
from api import rest
class BaseSchema(m.Schema):
    id = m.fields.Number(required=True, default=0)
    pr_status = m.fields.String(required=True, default=None)


class PullRequetStatusSchema(m.Schema):
    """The base model used to deserialize request parameters"""

    pull_requests = m.fields.Nested(BaseSchema)

   # OUTPUT will be in pull_requests = [ {'id': 1, 'pr_status': "Pending review"}, {...} ....]




pr_status = rest.model('pr_status', {
         'pr_id': fields.Integer(attribute='id'),
          'pr_status': fields.String(attribute='state')}
)

pr_status_output = rest.model('pr_status_output', {
    'prs_list' : fields.List(fields.Nested(pr_status), attribute="rows")
})
