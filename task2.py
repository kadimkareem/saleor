'''Are there any periods in which we get more issues?'''
import pandas as pd
import matplotlib.pylab as plt
 
issues=pd.read_json('./outputs/issues_json.json')

#get top issues over time
''' filter the data to get top issues over time '''
def get_top_issues_over_time():
    df=pd.DataFrame(issues)
    df['created_at'] = pd.to_datetime(df['created_at'])
    # group by date to count the number of issues created per day
    issues_per_day = df.groupby(df['created_at'].dt.date).size()
    #returns the index for the maximum value in each column
    max_issues_date = issues_per_day.idxmax()
    max_issues_count = issues_per_day.max()
   
    print(f'max_issues_date {max_issues_date} \n')
    print(f'ax_issues_coun {max_issues_count} \n')
    # TODO it calcualte dates not issues (max date not max issue)
            
 

def plot_created_at():
    plt.plot(cleaned_date_data())
    plt.show()
    
 
def cleaned_date_data():
    data=pd.DataFrame(issues)
    df=pd.DataFrame(data)
    #make it timeseries
    df['created_at'] =pd.to_datetime(data['created_at'])
    #remove time
    return df['created_at'].dt.date
   
     
 
def plot_top_issues():
    data=get_issue_count_per_day( )
    plt.figure(figsize=(10, 6))
    plt.plot(data['created_at'],data['count'], marker='o', linestyle='-')
    plt.title('top issues per day')
    plt.xlabel('date')
    plt.ylabel('issues count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
 
    
def get_issue_count_per_day():
    '''get the issue count per day'''
    data=cleaned_date_data()
    df = pd.DataFrame(data)
    # Count the occurrences of each row
    duplicate_issues = df.groupby(df.columns.tolist()).size().reset_index(name='count')
    duplicated_rows = duplicate_issues[duplicate_issues['count'] > 1]
    duplicated_rows.plot(kind='bar')
    plt.title('top issues per day')
    plt.xlabel('date')
    plt.ylabel('issues count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print(f' issues per day {duplicated_rows} \n')
    return duplicated_rows

 
def periods_with_higher_weekly_average():
    '''periods with higher than average '''
    df=get_issue_count_per_day()
    df['created_at']=pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)
    #sum issues per week
    issues_per_week=df.resample('W').sum()
    print(f'sum issues per week {issues_per_week}')
    plt.figure(figsize=(10, 6))
    issues_per_week['count'].plot(kind='bar')
    plt.title('top issues per week')
    plt.xlabel('date')
    plt.ylabel('issues count')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
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
    
   
    
        
    
 
  
    
    
    


def main():
    get_top_issues_over_time()
    #plot_top_issues()
    periods_with_higher_weekly_average()
    
    

if __name__=="__main__":
    main()