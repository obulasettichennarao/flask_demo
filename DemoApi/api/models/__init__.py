""" 
this file is used to write the Serialization/deserialition of API request & response 
we use marshallow module for field validation, formating and serializing, deserialization
"""
from api.models.pull_requests import PullRequetStatusSchema
from api.models.pull_requests import pr_status_output

__all__ = [

'PullRequetStatusSchema',
'pr_status_output'
]
