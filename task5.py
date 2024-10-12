import pandas as pd
from transformers import AutoTokenizer, BertForMaskedLM
import torch
from transformers import BertTokenizer

from task4 import get_most_popular_labels


data=pd.read_json('./outputs/issues_cleanded_label.json')
 
df = pd.DataFrame(data)
 
print(df['labels'].iloc[1:5])
# dd=pd.DataFrame(labels['count'],columns=['label'])
# descriptions =df['body']
# print(dd)

