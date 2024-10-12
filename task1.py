'''How do the number of issues evolve over time?'''


from  datetime import datetime 
import matplotlib.pylab as plot
from typing import List 
from common import read_json
from issue_model import Issue, model_from_json
import pandas as pandas

json_file=read_json(path='.dataset/issues_json.json')
issues:List[Issue]= model_from_json('.dataset/issues_json.json')
 
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

    # basic_plot(title= f'{title} evolvation',xlabel='date',ylabel='number of issues',
    #           imge_name=f'{title}_daily_evolve',xdata=evolvation.index,ydata=evolvation['count'],label=f'{len(evolvation.index)}')
    bar_plot(title= f'{title} evolvation',xlabel='date',ylabel='number of issues',
              image_name=f'{title}_daily_evolve',xdata=evolvation.index,ydata=evolvation['count'],label=f'{len(evolvation.index)}',data=describe)
    


 
    

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
     

def main():
     #measure_evolvation('D','daily')
     #measure_evolvation('W','weakly')
     measure_evolvation('ME','monthly')
 
if __name__=="__main__":
    main()