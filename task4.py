from typing import List
import pandas as pd
import matplotlib.pylab as plt

from issue_model import Label, model_from_json, model_to_json

issues= model_from_json('./outputs/issues_cleanded_label.json')
data=pd.read_json('./outputs/issues_cleanded_label.json')
df=pd.DataFrame(data)

def clean_issue_labels():
    issues= model_from_json(path='./outputs/issues_json.json')
    unpacked_labled_issue=[]
    for issue in issues:
        if len(issue.labels)>=1:
            issue_labels:List[Label]=issue.labels
            for label in issue_labels:
                issue.labels=label
                unpacked_labled_issue.append(issue)
            
            #remove empty labels issue
        elif len(issue.labels)==0:
            issues.remove(issue)
            
        else:
            
            unpacked_labled_issue.append(issue)
    model_to_json(model=unpacked_labled_issue,file_name='issues_cleanded_label')



def get_most_popular_labels():
    '''get most popular category'''
    labels=[]
    for issue in issues:
        labels.append(issue.labels.name)
     
     
     # Count occurrences of each name
    name_counts = pd.Series(labels).value_counts().reset_index()

    # Rename the columns
    name_counts.columns = ['name', 'count']

    # Display the DataFrame
    print(name_counts)
    print(set(labels))   

# print(f'show all list {get_most_popular_labels()}')
# print(f'most popular category is: { get_most_popular_labels().idxmax()} which is {get_most_popular_labels().max()}')

 
# get_most_popular_labels().plot(kind='bar')
# plt.show()


#clean label data , unpack multiple labeld issues

get_most_popular_labels()

