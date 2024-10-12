'''How do the number of issues evolve over time?'''

from  datetime import datetime 
import matplotlib.pylab as plot
from typing import List 
from common import read_json
from issue_model import Issue, model_from_json
import pandas as pandas
from plot_data import bar_plot

json_file=read_json(path='./dataset/issues_json.json')
issues:List[Issue]= model_from_json('./dataset/issues_json.json')
 
def get_issues_creation_date()->list[datetime]:
    issues_creation_dates = [issue.created_at.replace(tzinfo=None) for issue in issues]
    return issues_creation_dates

def date_data_frame():
    creation_date=get_issues_creation_date()
    df=pandas.DataFrame(creation_date,columns=['created_at'])
    df['count'] = 1  
    df.set_index('created_at', inplace=True)
    return df

def measure_evolvation(timedelta:str,title:str):
    '''plot  evolvation for each time interval [D for daily , W for weakly , ME for monthly]'''
    creation_date_frame=date_data_frame()
    evolvation = creation_date_frame.resample(timedelta).count()
    creation_date_frame.to_json(path_or_buf=f'./creation_dates/{title}_creation_date_frame.json')
    
    describe=evolvation.describe()
    print(evolvation)
    print(f'date max:{evolvation.idxmax()}')
    print(f'coutn mean:{evolvation.max()}')

    # basic_plot(title= f'{title} evolvation',xlabel='date',ylabel='number of issues',
    #           imge_name=f'{title}_daily_evolve',xdata=evolvation.index,ydata=evolvation['count'],label=f'{len(evolvation.index)}')
    bar_plot(title= f'{title} evolvation',xlabel='date',ylabel='number of issues',
              image_name=f'{title}_daily_evolve',xdata=evolvation.index,ydata=evolvation['count'],label=f'{len(evolvation.index)}',data=describe)
    

measure_evolvation('D','daily')
#measure_evolvation('W','weakly')
#measure_evolvation('ME','monthly')
 
 