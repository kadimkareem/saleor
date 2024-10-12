import json
def get_github_access_token():
    with open('access_token.json','r') as access_token_json_file:
        data=json.load(access_token_json_file)
        token=data['token']
        access_token=token
        return access_token


        
def read_json(path):
    '''read json file'''
    with open(path,'r') as issues_json:
        data = json.load(issues_json)
        return data
def read_json_pandas():
    
    issues=pd.read_json('./outputs/issues_json.json')
def main():
    print(get_github_access_token())

if __name__=="__main__":
    main()