

from  datetime import datetime 
import matplotlib.pylab as plot
from typing import List 
from common import read_json
from issue_model import Issue, model_from_json
import pandas as pandas


def bar_plot(title: str, xlabel: str, ylabel: str, image_name: str, xdata, ydata, label: str, data):
    fig, (ax1, ax2) = plot.subplots(2, 1, gridspec_kw={'height_ratios': [6, 2]}, figsize=(12, 8)) 
    
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

    # Rotate x-axis labels for readability
    ax1.set_xticklabels(xdata, rotation=45, ha='right')
    

 
    ax2.axis('off')
    ax2.axhline(y=0.99, color='black', linewidth=1)
    describe_table = data
    describe_text = describe_table.to_string()
    ax2.text(0.01, 0.90, describe_text, fontsize=8, ha='left', va='top', transform=ax2.transAxes, family='monospace')  # Adjusted scale
    plot.tight_layout()


    plot.savefig(f'./plots/{image_name}.png')
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