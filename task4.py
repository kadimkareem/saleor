from typing import List
import pandas as pd
import matplotlib.pylab as plt

from issue_model import Label, model_from_json, model_to_json
from plot_data import bar_plot

issues= model_from_json('./dataset/issues_cleanded_label.json')
data=pd.read_json('./dataset/issues_cleanded_label.json')
df=pd.DataFrame(data)

def clean_issue_labels():
    issues= model_from_json(path='./dataset/issues_json.json')
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
    
    print(name_counts)
    print(set(labels)) 
    return name_counts 


 
bar_plot(title='most popular label',xdata=get_most_popular_labels()['name'],ydata=get_most_popular_labels()['count'],xlabel='name',ylabel='issues',image_name='popular_label',data=get_most_popular_labels().describe(),label=f'{len(get_most_popular_labels())}')



get_most_popular_labels()

