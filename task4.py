from typing import List
import pandas as pd
import matplotlib.pylab as plt

from issue_model import Label, model_from_json, model_to_json


data=pd.read_json('./outputs/issues_json.json')

def clean_issue_labels():
    issues= model_from_json(path='./outputs/issues_json.json')
    unpacked_labled_issue=[]
    for issue in issues:
        if len(issue.labels)>1:
            issue_labels:List[Label]=issue.labels
            for label in issue_labels:
                issue.labels=label
                unpacked_labled_issue.append(issue)
            
        else:
            unpacked_labled_issue.append(issue)
    model_to_json(model=unpacked_labled_issue,file_name='issues_cleanded_label')

df = clean_issue_labels()
def get_most_popular_labels():
    '''get most popular category'''
    print(df)
    
    #get label names list for each issue
    label_names = df['labels'].apply(lambda labels: [label['name'] for label in labels])
  
    flattened_labels = [label for sublist in label_names for label in sublist]
    label_df = pd.DataFrame(flattened_labels, columns=['label_name'])

    # Count the occurrences of each label name
    label_counts = label_df['label_name'].value_counts().reset_index()
    label_counts.columns = ['label', 'count'] 
    
    return label_counts

# print(f'show all list {get_most_popular_labels()}')
# print(f'most popular category is: { get_most_popular_labels().idxmax()} which is {get_most_popular_labels().max()}')

 
# get_most_popular_labels().plot(kind='bar')
# plt.show()


#clean label data , unpack multiple labeld issues

clean_issue_labels()

