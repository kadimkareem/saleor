import json
from typing import List, Optional
from pydantic import BaseModel, HttpUrl, parse_obj_as
from pathlib import Path
from datetime import datetime

'''convert issue to models helps to validate date so we get validated data , and in development able us to use code hints'''
class User(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    gravatar_id: str
    url: HttpUrl
    html_url: HttpUrl
    followers_url: HttpUrl
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: str
    received_events_url: HttpUrl
    type: str
    site_admin: bool

class Label(BaseModel):
    id: int
    node_id: str
    url: HttpUrl
    name: str
    color: str
    default: bool
    description: Optional[str] = None

class PullRequest(BaseModel):
    url: HttpUrl
    html_url: HttpUrl
    diff_url: HttpUrl
    patch_url: HttpUrl
    merged_at: Optional[datetime] = None

class Reactions(BaseModel):
    url: HttpUrl
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
    url: HttpUrl
    repository_url: HttpUrl
    labels_url: str
    comments_url: HttpUrl
    events_url: HttpUrl
    html_url: HttpUrl
    id: int
    node_id: str
    number: int
    title: str
    user: User
    labels: List[Label]
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
    timeline_url: HttpUrl
    performed_via_github_app: Optional[str] = None
    state_reason: Optional[str] = None

