import json
from typing import List, Optional
from pydantic import BaseModel, Json, parse_obj_as
 
from datetime import datetime

from common import read_json

'''convert issue to models helps to validate date so we get validated data , and in development able us to use code hints'''
class User(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool

class Label(BaseModel):
    id: int
    node_id: str
    url: str
    name: str
    color: str
    default: bool
    description: Optional[str] = None

class PullRequest(BaseModel):
    url: str
    html_url: str
    diff_url: str
    patch_url: str
    merged_at: Optional[datetime] = None

class Reactions(BaseModel):
    url: str
    total_count: int
    plus_one: int = 0
    minus_one: int = 0
    laugh: int = 0
    hooray: int = 0
    confused: int = 0
    heart: int = 0
    rocket: int = 0
    eyes: int = 0

class Issue(BaseModel):
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    id: int
    node_id: str
    number: int
    title: str
    user: User
    labels: List[Label] | Label
    state: str
    locked: bool
    assignee: Optional[User] = None
    assignees: List[User]
    milestone: Optional[str] = None
    comments: int
    created_at: datetime
    updated_at: datetime
    closed_at: Optional[datetime] = None
    author_association: str
    active_lock_reason: Optional[str] = None
    draft: Optional[bool] = None
    pull_request: Optional[PullRequest] = None
    body: Optional[str] = None
    closed_by: Optional[User] = None
    reactions: Reactions
    timeline_url: str
    performed_via_github_app: Optional[str] = None
    state_reason: Optional[str] = None

def model_from_json(path:str) ->List[Issue]:
        '''Parse the JSON data into a list of Issue objects using Pydantic'''
        data=read_json(path=path)
        issues = parse_obj_as(List[Issue], data)
        return issues

def model_to_json(model:List[Issue],file_name:str):

    data=[j.model_dump(mode='json') for j in model]
    with open(f'./outputs/{file_name}.json','w') as json_file:
        json.dump(data,json_file,indent=4)
      