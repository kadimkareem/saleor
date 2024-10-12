'''How do the number of issues evolve over time?'''


from  datetime import datetime 
import matplotlib.pylab as plot
from typing import List 
from common import read_json
from issue_model import Issue
from statistic import model_from_json
import pandas as pandas

json_file=read_json(path='./outputs/issues_json.json')
issues:List[Issue]= model_from_json(data=json_file)
 
def get_issues_creation_date()->list[datetime]:
    issues_creation_dates = [issue.created_at for issue in issues]
    issues_creation_dates.sort()
    print(issues_creation_dates)
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
    creation_date_frame.to_json(path_or_buf=f'{title}_creation_date_frame.json')
    describe=evolvation.describe()
    

    # basic_plot(title= f'{title} evolvation',xlabel='date',ylabel='number of issues',
    #           imge_name=f'{title}_daily_evolve',xdata=evolvation.index,ydata=evolvation['count'],label=f'{len(evolvation.index)}')
    bar_plot(title= f'{title} evolvation',xlabel='date',ylabel='number of issues',
              image_name=f'{title}_daily_evolve',xdata=evolvation.index,ydata=evolvation['count'],label=f'{len(evolvation.index)}',data=describe)
    
def cumulative_evolve_plot():
    '''plot cumulative'''
    df=pandas.DataFrame(data=get_issues_creation_date(),columns=['created_date'])
    df.set_index(df['created_date'],inplace=True)
    print(df['created_date'])
    time_series = df.resample('D').size()

    # Plotting the time series
    plot.figure(figsize=(10, 6))
    plot.plot(time_series.index, time_series, marker='o')
    plot.title('Time Series: Event Count Per Minute')
    plot.xlabel('Timestamp')
    plot.ylabel('Frequency')
    plot.xticks(rotation=45)
    plot.tight_layout()
    plot.show()

 
    

def basic_plot(title:str,xlabel:str,ylabel:str,imge_name,xdata:any,ydata:any,label:str):
    
    plot.figure(figsize=(10, 6),)
    plot.plot(xdata,ydata, marker='.', linestyle='-')
    plot.title(title)
    plot.xlabel(xlabel=xlabel)
    plot.ylabel(ylabel=ylabel)
    plot.grid(True)
    plot.savefig(f'./plots/{imge_name}.png')
    plot.show()
    
def bar_plot(title: str, xlabel: str, ylabel: str, image_name: str, xdata, ydata, label: str, data):
    fig, (ax1, ax2) = plot.subplots(2, 1, gridspec_kw={'height_ratios': [6, 2]}, figsize=(10, 6))
    
    bars_calculate = ax1.bar(xdata, ydata, color='skyblue', edgecolor='black', label=label)
 
    for bar in bars_calculate:
        height = bar.get_height()
        ax1.annotate(f'{int(height)}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

    ax1.set_title(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.legend()
 
    ax2.axis('off')
    ax2.axhline(y=0.99, color='black', linewidth=1, )
    describe_table = data
    describe_text = describe_table.to_string()
    ax2.text(0.01, 0.90, describe_text, fontsize=8, ha='left', va='top', transform=ax2.transAxes,
             family='monospace') # Adjust scale if needed for readability
 
    plot.tight_layout()
    plot.savefig(f'./plots/{image_name}.png')
    plot.show()
     
def overall():
    data = date_data_frame()
    daily_changes = data.resample('D').sum()
    weekly_changes = data.resample('W').sum()
    monthly_changes = data.resample('M').sum()

    # Create subplots with gridspec to have the main plot and the table below it
    fig, (ax1, ax2) = plot.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(10, 8))

    # Main plot (bar charts for daily, weekly, and monthly data)
    ax1.bar(daily_changes.index, daily_changes['count'], color='skyblue', edgecolor='black', label=f'Daily ({len(daily_changes)})')
    ax1.bar(weekly_changes.index, weekly_changes['count'], color='green', edgecolor='black', label=f'Weekly ({len(weekly_changes)})')
    ax1.bar(monthly_changes.index, monthly_changes['count'], color='blue', edgecolor='black', label=f'Monthly ({len(monthly_changes)})')

    # Set titles and labels for the main plot
    ax1.set_title('Issues Data Change Over Time')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Count')
    ax1.legend()

    # Turn off the axis for the table
    ax2.axis('off')

    # Create a table from the data.describe().T output and add it to the subplot
    describe_table = data.describe().T
    table = ax2.table(cellText=describe_table.values,
                      colLabels=describe_table.columns,
                      rowLabels=describe_table.index,
                      cellLoc='center', 
                      loc='center')

    table.scale(1, 1.5)  # Adjust scale if needed for readability
    table.auto_set_font_size(False)
    table.set_fontsize(10)

    # Adjust layout to make everything fit nicely
    plot.tight_layout()

    # Save the figure
    plot.savefig('./plots/overall.png')

    # Show the figure
    plot.show()
def main():
    measure_evolvation('D','daily')
    measure_evolvation('W','weakly')
    measure_evolvation('ME','monthly')
    cumulative_evolve_plot()
    #overall()
if __name__=="__main__":
    main()