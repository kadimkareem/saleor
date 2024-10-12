'''Is there anyone who reports more issues than others'''
import pandas as pd


issues=pd.read_json('./outputs/issues_json.json')


def get_issues_by_user():
    df = pd.DataFrame(issues)

    user_logins = df['user'].apply(lambda x: x['login'])

    # get the data for max
    top_user = user_logins.value_counts().idxmax()
    # get the numirce max
    top_user_issues_count = user_logins.value_counts().max()

    print(f"user who reports more issues than others is : '{top_user}', with {top_user_issues_count} issues.")


def main():
    get_issues_by_user()
    
if __name__=="__main__":
    main()
