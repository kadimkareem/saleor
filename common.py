import json
def get_github_access_token():
    with open('access_token.json','r') as access_token_json_file:
        data=json.load(access_token_json_file)
        token=data['token']
        access_token=token
        return access_token


def main():
    print(get_github_access_token())

if __name__=="__main__":
    main()