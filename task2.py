'''Are there any periods in which we get more issues?'''
import pandas as pd
import matplotlib.pylab as plt
from plot_data import bar_plot
 
issues=pd.read_json('./dataset/issues_json.json')

 
def cleaned_date_data():
    data=pd.DataFrame(issues)
    df=pd.DataFrame(data)
    #make it timeseries
    df['created_at'] =pd.to_datetime(data['created_at'])
    #remove time
    return df['created_at'].dt.date
      
    
def get_issue_count_per_day():
    '''get the issue count per day'''
    data=cleaned_date_data()
    df = pd.DataFrame(data)
    # Count the occurrences of each row
    duplicate_issues = df.groupby(df.columns.tolist()).size().reset_index(name='count')
    duplicated_rows = duplicate_issues[duplicate_issues['count'] > 1]
    return duplicated_rows

 
def periods_with_higher_weekly_average():
    '''periods with higher than average '''
    df=get_issue_count_per_day()
    df['created_at']=pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)
    #sum issues per week
    issues_per_week=df.resample('W').sum()
    print(f'sum issues per week {issues_per_week}')
    bar_plot(xdata=issues_per_week.index,
             ydata=issues_per_week['count'],
             title='periods_with_higher_weekly_average',
             xlabel='date',
             ylabel='count',
             label=f'{len(issues_per_week.index)}',
             image_name='periods_with_higher_weekly_average',
             data=issues_per_week.describe()
             )

    #weekly average 
    mean_data=issues_per_week['count'].mean()
    print(f'mean issues per week {mean_data} \n')
    std_data=issues_per_week['count'].std()
    print(f'std issues per week {std_data} \n')
  
    #periods where the number of issues  significantly higher than the average
    high_weekly_issue_periods = issues_per_week[issues_per_week['count'] > mean_data + std_data]
    #weekly issues sum bigger than average
    high_issue_bigger_than_average = issues_per_week[issues_per_week['count'] > mean_data ]
    print(f' high weekly issue periods {high_weekly_issue_periods} \n')
    print(f'high issue bigger than average {high_issue_bigger_than_average} \n')
    
    
periods_with_higher_weekly_average()
