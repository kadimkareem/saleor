import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from issue_model import model_from_json


 
data=pd.read_json('./dataset/issues_cleanded_label.json')
df=pd.DataFrame(data)

df=df.sample(10)
issues=model_from_json('./dataset/issues_cleanded_label.json')
#remove other coukmns
df=df[['labels','body']]
#keep only name in lables
df['labels']=df['labels'].apply(lambda x: x['name'])

 

# Tokenization and label encoding for multi-class classification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
label_encoder = LabelEncoder()
df['labels'] = label_encoder.fit_transform(df['labels'])

# Custom Dataset
class TextClassificationDataset(Dataset):
    def __init__(self, df, tokenizer, max_length=512):
        self.df = df
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        inputs = self.tokenizer(
            self.df.iloc[idx]['body'],
            add_special_tokens=True,
            truncation=True,
            max_length=self.max_length,
            padding='max_length',
            return_tensors='pt'
        )
        labels = torch.tensor(self.df.iloc[idx]['labels'], dtype=torch.long)
        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'labels': labels
        }

# Model setup
num_labels = len(label_encoder.classes_)  # Get the number of unique labels
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=num_labels)

# DataLoader
dataloader = DataLoader(TextClassificationDataset(df, tokenizer), batch_size=8, shuffle=True)

# Optimizer and training loop
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
model.train()
for epoch in range(3):  
    for batch in dataloader:
        optimizer.zero_grad()
        outputs = model(
            input_ids=batch['input_ids'],
            attention_mask=batch['attention_mask'],
            labels=batch['labels']
        )
        loss = outputs.loss
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Prediction function
def predict(text, model, tokenizer):
    model.eval()
    inputs = tokenizer(text, add_special_tokens=True, truncation=True, max_length=512, padding='max_length', return_tensors='pt')
    with torch.no_grad():
        outputs = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
    predicted_label = torch.argmax(outputs.logits, dim=1).item()
    return label_encoder.inverse_transform([predicted_label])[0]

# Example prediction
print(predict("v2 is deprecated and will be removed", model, tokenizer))