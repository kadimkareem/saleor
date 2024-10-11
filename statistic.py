import json
from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Json, parse_obj_as
from pathlib import Path
from datetime import datetime

from issue_model import Issue

issues_path = Path('./outputs/issues_json.json')

def read_json(path):
    '''read json file'''
    with path.open('r') as issues_json:
        data = json.load(issues_json)
        return data


def model_from_json() ->Json:
        '''Parse the JSON data into a list of Issue objects using Pydantic'''
        data=read_json(path=issues_path)
        issues = parse_obj_as(List[Issue], data)
        return issues



def get_issues_count(issues: List[Issue]):
    print(f"Total number of issues: {len(issues)}")

def main():
    issues = model_from_json(issues_path)
    get_issues_count(issues)
    # Example of accessing details of the first issue to check the data
    if issues:
        print(f"First issue title: {issues[0].title}")
        print(f"First issue user: {issues[0].user.avatar_url}")

if __name__ == "__main__":
    main()